async function buttonClick() {
    const response = await fetch('/api/image', {
        method: 'GET'
    })
    const data = await response.json()
    const image_url = data.image_url
    document.body.style.backgroundImage = `url('${image_url}')`
}

async function createUser() {
    const response = await fetch('/api/user/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: 'John Doe',
            email: 'johndoe@gmail.com'
        })
    })
}