async function buttonClick() {
    const response = await fetch('/api/image', {
        method: 'GET'
    })
    const data = await response.json()
    const image_url = data.image_url
    document.body.style.backgroundImage = `url('${image_url}')`
}