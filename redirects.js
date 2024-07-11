const fs = require('fs');
const yaml = require('js-yaml');
const path = require('path');

// Load redirects from _redirects.yml
const redirectsFile = fs.readFileSync('_redirects.yml', 'utf8');
const redirects = yaml.safeLoad(redirectsFile).redirects;

// Ensure the _redirects directory exists
const redirectsDir = path.join(__dirname, '_redirects');
if (!fs.existsSync(redirectsDir)) {
    fs.mkdirSync(redirectsDir);
}

// Generate markdown files for each redirect
redirects.forEach(redirect => {
    const fromPaths = redirect.from;
    const toUrl = redirect.to;

    fromPaths.forEach(fromPath => {
        const trimmedPath = fromPath.trim('/');
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
