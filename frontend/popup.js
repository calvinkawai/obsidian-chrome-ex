async function createTags() {
  const [tab] = await chrome.tabs.query({
    active: true,
    lastFocusedWindow: true,
  });

  console.log("tab: ", tab.url);
  title = document.getElementById("title").value;
  tags = document.getElementById("tags").value;
  data = JSON.stringify({
    title: title,
    tags: tags,
    url: tab.url,
  });

  await fetch("http://127.0.0.1:8090/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      accept: "application/json",
    },
    body: data,
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.message);
      document.getElementById("title").value = "";
      document.getElementById("tags").value = "";
    })
    .catch((error) => alert(error));
}

document
  .getElementById("createTagsForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const tags = document.getElementById("tags").value;
    const title = document.getElementById("title").value;

    createTags(tags, title);
  });
