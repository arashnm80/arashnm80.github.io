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
                console.error(`Error: File with unsupported extension found: ${file}`);
            } else if (ext === '') {
                console.error(`Error: File without extension found: ${file}`);
            }
        });

        fs.writeFileSync(outputFile, quotes, 'utf8');
        console.log(`Quotes have been extracted to ${outputFile}`);
    });
};

// Execute the function
extractQuotes(directoryPath, outputFilePath);