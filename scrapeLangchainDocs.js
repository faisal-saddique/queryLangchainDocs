// Import required libraries
const fs = require('fs').promises;  // File system module for handling file operations asynchronously
const axios = require('axios');  // HTTP client for making API requests
const cheerio = require('cheerio');  // Library for parsing and manipulating HTML content
const TurndownService = require('turndown');  // Library for converting HTML to Markdown

// Function to scrape a website, convert HTML to Markdown, and save the content to files
async function scrapeAndSaveMarkdown(url, outputDirectory, visited = new Set(), baseUrl) {
  // If the URL has already been visited, return without reprocessing
  if (visited.has(url)) {
    return;
  }

  // Mark the current URL as visited
  visited.add(url);

  try {
    // Fetch the HTML content of the target website
    const response = await axios.get(url);
    const htmlContent = response.data;

    // Load the HTML content into cheerio for parsing
    const $ = cheerio.load(htmlContent);

    // Find the element with class "markdown" and get its inner HTML (Markdown content)
    const markdownContent = $('.markdown').html();

    // Use Turndown to convert the HTML back to Markdown
    const turndownService = new TurndownService();
    let markdownText = turndownService.turndown(markdownContent);

    // Remove \u200b characters from the markdown text (unicode character: Zero Width Space)
    markdownText = markdownText.replace(/\u200b/g, '');

    // Remove base64 images from the markdown text
    markdownText = markdownText.replace(/!\[.*?\]\(data:image\/.*?;base64,.*?\)/g, '');

    // Remove indents from code blocks
    markdownText = markdownText.replace(/```([\s\S]*?)```/g, (match, codeBlock) => {
      // Remove leading spaces from each line in the code block
      const lines = codeBlock.split('\n').map(line => line.replace(/^\s{4}/, ''));
      return '```\n' + lines.join('\n') + '\n```';
    });

    // Create the output directory if it doesn't exist
    await fs.mkdir(outputDirectory, { recursive: true });

    // Create a unique name for the Markdown file based on the URL
    let uniqueName = url.substring(baseUrl.length).trim().replace(/\//g, '_') + '.md';

    // Remove the underscore from the start of the filename if present
    if (uniqueName.startsWith('_')) {
      uniqueName = uniqueName.slice(1);
    }

    // Create the output file path using the output directory and the unique name
    const outputFilePath = outputDirectory + '/' + uniqueName;

    // Save the scraped content to the file
    await fs.writeFile(outputFilePath, markdownText);

    // Log the successful scraping and file-saving details
    console.log('Scraping completed for URL:', url);
    console.log('Markdown content saved to:', outputFilePath);

    // Extract links from the HTML content
    const links = $('a')
      .map((i, el) => $(el).attr('href'))
      .get()
      .filter(link => link && !link.includes('#'))
      .map(link => new URL(link, url).href)
      .filter(link => link.startsWith(baseUrl))
      .map(link => link.replace(/\.html$/, ''));

    // Recursively scrape and save the Markdown content for the extracted links
    const promises = links.map(link => scrapeAndSaveMarkdown(link, outputDirectory, visited, baseUrl));
    await Promise.all(promises);

  } catch (error) {
    console.error(`Error during scraping ${url}:`, error);
  }
}

// Example usage:
const targetUrl = 'https://python.langchain.com/docs/get_started/introduction';
const baseUrl = new URL(targetUrl).origin;

const outputDirectory = './langchain_docs_python'; // Replace with the desired output directory path

// Start the scraping process with the target URL and output directory
scrapeAndSaveMarkdown(targetUrl, outputDirectory, undefined, baseUrl).then(() => {
  console.log('Done scraping links');
});
