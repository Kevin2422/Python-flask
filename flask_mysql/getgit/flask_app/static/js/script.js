
    async function getCoderData() {
            var input = document.querySelector('#input');
            var heading = document.querySelector('#hello')
            // The await keyword lets js know that it needs to wait until it gets a response back to continue.
            var response = await fetch("https://api.github.com/users/" + input.value);
            // We then need to convert the data into JSON format.
            var coderData = await response.json();
            console.log(coderData)
            console.log(coderData)
            console.log(coderData.avatar_url);
            var image = document.querySelector('#avatar')
            image.src = coderData.avatar_url
            heading.innerText = `${coderData.name}` + ' has '  + `${coderData.following}` + ' follower(s)'
            return coderData
        }
            
       