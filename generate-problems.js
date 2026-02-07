const fs = require('fs');
const path = require('path');

// Get all directories in the current folder
const directories = fs.readdirSync(__dirname, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory())
    .filter(dirent => !dirent.name.startsWith('.')) // Exclude hidden folders like .git
    .map(dirent => dirent.name);

const problems = [];

directories.forEach(dir => {
    // Parse directory name (format: "number-problem-name")
    const match = dir.match(/^(\d+)-(.+)$/);
    if (!match) return; // Skip if doesn't match pattern

    const [, idStr, slug] = match;
    const id = parseInt(idStr);
    
    // Convert slug to readable name
    const name = slug
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');

    // Find solution file
    const dirPath = path.join(__dirname, dir);
    const files = fs.readdirSync(dirPath);
    const solutionFile = files.find(f => f !== 'README.md' && !f.startsWith('.'));

    // Extract difficulty from README.md
    let difficulty = 'Unknown';
    const readmePath = path.join(dirPath, 'README.md');
    if (fs.existsSync(readmePath)) {
        const readmeContent = fs.readFileSync(readmePath, 'utf8');
        if (readmeContent.includes('Difficulty-Easy')) difficulty = 'Easy';
        else if (readmeContent.includes('Difficulty-Medium')) difficulty = 'Medium';
        else if (readmeContent.includes('Difficulty-Hard')) difficulty = 'Hard';
    }

    problems.push({
        id,
        slug: dir,
        name,
        difficulty,
        solutionFile: solutionFile || null
    });
});

// Sort by problem ID
problems.sort((a, b) => a.id - b.id);

// Write to problems.json
fs.writeFileSync(
    path.join(__dirname, 'problems.json'),
    JSON.stringify(problems, null, 2),
    'utf8'
);

console.log(`✅ Generated problems.json with ${problems.length} problems`);
console.log(`📊 Easy: ${problems.filter(p => p.difficulty === 'Easy').length}`);
console.log(`📊 Medium: ${problems.filter(p => p.difficulty === 'Medium').length}`);
console.log(`📊 Hard: ${problems.filter(p => p.difficulty === 'Hard').length}`);
