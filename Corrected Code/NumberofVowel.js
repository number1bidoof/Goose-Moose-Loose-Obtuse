function countVowels(vowelsting) {
    const vowels = "aeiouAEIOU";
    let count = 0;
    for (let i of vowelsting) {
        if (vowels.includes(i)) {
            count++;
        }
    }
    console.log(count);
}

countVowels("Hello World, I really need to finish this assigment")
