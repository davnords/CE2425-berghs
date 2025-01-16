async function generateImage() {
    const response = await fetch('/api/image', {
        method: 'GET'
    });
    const data = await response.json();
    const image_url = data.image_url;

    
    const imageElement = document.getElementById("generatedImage");
    imageElement.src = image_url;
}

