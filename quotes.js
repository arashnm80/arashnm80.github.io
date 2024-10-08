const fs = require('fs');
const path = require('path');

const fileTitle = "---\nlayout: page\ntitle: Quotes\n---\n\n"

// Directory containing markdown files
const directoryPath = path.join(__dirname, 'crapbook');

// Output file
const outputFilePath = path.join(__dirname, 'quotes.md');

// ANSI escape codes for colors
const RED = '\x1b[31m';
const RESET = '\x1b[0m';

// Function to log errors in red
const logError = (message) => {
    console.error(`${RED}${message}${RESET}`);
};

// Function to extract quotes from markdown files
const extractQuotes = (directory, outputFile) => {
    fs.readdir(directory, (err, files) => {
        if (err) {
            return logError('Unable to scan directory: ' + err);
        }

        let quotes = '';
        quotes += fileTitle;

        files.forEach((file) => {
            const filePath = path.join(directory, file);
            const ext = path.extname(file);

            if (ext === '.md') {
                const data = fs.readFileSync(filePath, 'utf8');

                const lines = data.split('\n');
                lines.forEach((line) => {
                    if (line.startsWith('> ')) {
                        line = line.replace(/\[(.*?)\]\(.*?\)/g, '$1'); // remove markdown links
                        line = line.replace(/\*\*/g, ''); // remove every "**" if text is bold
                        quotes += line + '\n\n';
                    }
                });
            } else if (ext !== '' && ext !== '.md') {
                logError(`Error: File with unsupported extension found: ${file}`);
            } else if (ext === '') {
                logError(`Error: File without extension found: ${file}`);
            }
        });

        fs.writeFileSync(outputFile, quotes, 'utf8');
        console.log(`Quotes have been extracted to ${outputFile}`);
    });
};

// Execute the function
extractQuotes(directoryPath, outputFilePath);