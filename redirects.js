const fs = require('fs');
const yaml = require('js-yaml');
const path = require('path');

// Load redirects from _redirects.yml
const redirectsFile = fs.readFileSync('_redirects.yml', 'utf8');
const redirects = yaml.load(redirectsFile).redirects;

// Ensure the _redirects directory exists
const redirectsDir = path.join(__dirname, '_redirects');
if (!fs.existsSync(redirectsDir)) {
    fs.mkdirSync(redirectsDir);
}

// Delete all previous files in _redirects
fs.readdirSync('_redirects').forEach(file => {
    const filePath = path.join(directory, file);
    fs.unlinkSync(filePath);
    console.log(`Deleted ${filePath}`);
});

// Generate markdown files for each redirect
redirects.forEach(redirect => {
    const fromPaths = Array.isArray(redirect.from) ? redirect.from : [redirect.from];
    const toUrl = redirect.to;

    fromPaths.forEach(fromPath => {
        const trimmedPath = fromPath.replace(/^\//, '').replace(/\/$/, ''); // Remove leading and trailing slashes
        const filename = path.join(redirectsDir, `${trimmedPath}.md`);

        // Create markdown content
        const content = `---
layout: null
permalink: ${fromPath}
redirect_to: ${toUrl}
---`;

        // Write the content to the markdown file
        fs.writeFileSync(filename, content, 'utf8');
    });
});

console.log('Redirect markdown files generated successfully.');
