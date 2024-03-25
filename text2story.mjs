import fs from "fs/promises";


const files = await fs.readdir('./text')

const test = []
const train = []

let count = 0;

for (let file of files) {
    const story = await fs.readFile('./text/' + file, 'utf8')
    count++ % 2 === 0 ? test.push({ story }) : train.push({ story })
}

await fs.writeFile('./data/BGStories/data00.json', JSON.stringify(test))
await fs.writeFile('./data/BGStories/data01.json', JSON.stringify(train))

