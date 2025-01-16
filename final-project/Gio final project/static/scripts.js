async function fortuneGeneration() {
    const response = await fetch('/api/fortune', {
        method: 'GET'
    })
    const data = await response.json()
    document.getElementById('fortuneText').innerHTML = data.text
}