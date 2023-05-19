var postForm = document.getElementById("post-form");
var postList = document.getElementById("post-list");

postForm.addEventListener("submit", function (event) {
    event.preventDefault();
    var post = document.getElementById("post").value;
    var author = fname ;
    var date = new Date().toLocaleString();
    var newpost = document.createElement("div");
    newpost.classList.add("post");
    newpost.innerHTML = '<p class="author">' + author + '</p><p>' + post + '</p><p class="date">' + date + '</p>';
    var likeButton = document.createElement("button");
    likeButton.classList.add("like-button");
    likeButton.innerHTML = "Like";
    var likeCount = 0;
    likeButton.addEventListener("click", function () {
        likeCount++;
        likeButton.innerHTML = "Liked (" + likeCount + ")";
        likeButton.classList.add("liked");
        likeButton.disabled = true;
    });
    newpost.appendChild(likeButton);
    var photo = document.getElementById("photo").files[0];
    if (photo) {
        var image = document.createElement("img");
        image.src = URL.createObjectURL(photo);
        image.classList.add("image");
        newpost.insertBefore(image, newpost.firstChild);
    }
    postList.insertBefore(newpost, postList.firstChild);
    document.getElementById("post-form").reset();
    document.querySelector(".no-posts").style.display = "none";
});
