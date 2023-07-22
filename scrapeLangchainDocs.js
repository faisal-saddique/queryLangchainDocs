const fs = require('fs').promises;
const axios = require('axios');
const cheerio = require('cheerio');
const TurndownService = require('turndown');

async function scrapeAndSaveMarkdown(url, outputDirectory, visited = new Set(), baseUrl) {
  if (visited.has(url)) {
    return;
  }

  visited.add(url);

  try {
    // Fetch the HTML content of the target website
    const response = await axios.get(url);
    const htmlContent = response.data;

    // Load the HTML content into cheerio for parsing
    const $ = cheerio.load(htmlContent);

    // Find the element with class "markdown" and get its inner HTML
    const markdownContent = $('.markdown').html();

    // Use Turndown to convert the HTML back to Markdown
    const turndownService = new TurndownService();
    const markdownText = turndownService.turndown(markdownContent);

    // Create the output directory if it doesn't exist
    await fs.mkdir(outputDirectory, { recursive: true });

    // Create a unique name for the Markdown file
    let uniqueName = url.substring(baseUrl.length).trim().replace(/\//g, '_') + '.md';
    
    // Remove the underscore from the start of the filename
    if (uniqueName.startsWith('_')) {
      uniqueName = uniqueName.slice(1);
    }
    
    const outputFilePath = outputDirectory + '/' + uniqueName;

    // Save the scraped content to the file
    await fs.writeFile(outputFilePath, markdownText);

    console.log('Scraping completed for URL:', url);
    console.log('Markdown content saved to:', outputFilePath);

    const links = $('a')
      .map((i, el) => $(el).attr('href'))
      .get()
      .filter(link => link && !link.includes('#'))
      .map(link => new URL(link, url).href)
      .filter(link => link.startsWith(baseUrl))
      .map(link => link.replace(/\.html$/, ''));
    
    const promises = links.map(link => scrapeAndSaveMarkdown(link, outputDirectory, visited, baseUrl));
    await Promise.all(promises);

  } catch (error) {
    console.error(`Error during scraping ${url}:`, error);
  }
}

// Example usage:
const targetUrl = 'https://docs.langchain.com/docs';
const baseUrl = new URL(targetUrl).origin;

const outputDirectory = './langchain_docs'; // Replace with the desired output directory path

scrapeAndSaveMarkdown(targetUrl, outputDirectory, undefined, baseUrl).then(() => {
  console.log('Done scraping links');
});
