const fs = require('fs');
const path = require('path');

const fileTitle = "---\nlayout: page\ntitle: Quotes\n---\n\n"

// Directory containing markdown files
const directoryPath = path.join(__dirname, 'handbook');

// Output file
const outputFilePath = path.join(__dirname, 'quotes.md');

// Function to extract quotes from markdown files
const extractQuotes = (directory, outputFile) => {
    fs.readdir(directory, (err, files) => {
        if (err) {
            return console.error('Unable to scan directory:', err);
        }

        let quotes = '';
        quotes += fileTitle;

        files.forEach((file) => {
            if (path.extname(file) === '.md') {
                const filePath = path.join(directory, file);
                const data = fs.readFileSync(filePath, 'utf8');

                const lines = data.split('\n');
                lines.forEach((line) => {
                    if (line.startsWith('> ')) {
                        line = line.replace(/\[(.*?)\]\(.*?\)/g, '$1'); // remove markdown links
                        line = line.replace(/^(\*\*)(.*?)(\*\*)$/, '$2'); // remove "**" if it exists at the beginning and end of line (text is all bold)
                        quotes += line + '\n\n';
                    }
                });
            }
        });

        fs.writeFileSync(outputFile, quotes, 'utf8');
        console.log(`Quotes have been extracted to ${outputFile}`);
    });
};

// Execute the function
extractQuotes(directoryPath, outputFilePath);
