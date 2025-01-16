async function answerGeneration() {
    const response = await fetch('/api/answer', {
        method: 'GET'
    })
    const data = await response.json()
    document.getElementById('answerText').innerHTML = data.text
}