const fs = require('fs');
const axios = require('axios');
const cheerio = require('cheerio');
const TurndownService = require('turndown');

async function scrapeAndSaveMarkdown(url, outputDirectory, visited = new Set()) {
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
    if (!fs.existsSync(outputDirectory)) {
      fs.mkdirSync(outputDirectory, { recursive: true });
    }

    // Create a unique name for the Markdown file
    const baseUrl = 'https://python.langchain.com/docs';
    const uniqueName = url.substring(baseUrl.length).trim().replace(/\//g, '_') + '.md';
    const outputFilePath = outputDirectory + '/' + uniqueName;

    // Save the scraped content to the file
    fs.writeFileSync(outputFilePath, markdownText);

    console.log('Scraping completed for URL:', url);
    console.log('Markdown content saved to:', outputFilePath);

    const links = $('a')
      .map((i, el) => $(el).attr('href'))
      .get()
      .filter(link => link && !link.includes('#'))
      .map(link => new URL(link, url).href)
      .filter(link => link.startsWith(baseUrl))
      .map(link => link.replace(/\.html$/, ''));
    
    for (const link of links) {
      if (!visited.has(link)) {
        await scrapeAndSaveMarkdown(link, outputDirectory, visited);  
      }
    }

  } catch (error) {
    console.error(`Error during scraping ${url}:`, error);
  }
}

// Example usage:
const baseUrl = 'https://python.langchain.com/docs';
const targetUrl = `${baseUrl}/get_started/introduction`;
const outputDirectory = './langchain_python_docs'; // Replace with the desired output directory path

scrapeAndSaveMarkdown(targetUrl, outputDirectory).then(() => {
  console.log('Done scraping links');
});
