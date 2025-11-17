let htmxContent = document.querySelector("#htmx-content");
let innerTitle = document.querySelector(".innerTitle")


async function getArticlesPath() {
try {
    const response = await fetch('/articles.json');
    const data = await response.json();
    console.log(data);
    return data;
} catch (err) {
    console.error('Erro ao carregar artigos:', err);
    return [];
}
}

async function injectArticles(articlesArr){

    htmxContent.innerHTML = ""

    articlesArr = orderByUnix(articlesArr);

    for (const article of articlesArr) {
    const articleHtml = await buildHtmlArticle(article);
    htmxContent.innerHTML += articleHtml;
    }

}


async function buildHtmlArticle(article){

    let articleImg = await fetchBanner(`${article.path}`).then(bannerHtml => {
        if (bannerHtml) {
            return bannerHtml
        }
    });



    html = `
        <div class="articlesContainer">
        
            <img onclick="location.href='${article.path}'" src="${articleImg}" alt="">
        
        
        <div>
            <h1 onclick="location.href='${article.path}'">
                ${article.title}
            </h1>
            <p onclick="location.href='${article.path}'">
                ${article.chamada}
            </p>
        </div>
    </div>
    `

    return html
}



function orderByUnix(articlesArr) {
  if (!Array.isArray(articlesArr)) return [];
  return articlesArr.sort((a, b) => b.unixtime - a.unixtime);
}

async function fetchBanner(url) {
  try {
    const response = await fetch(url);
    const htmlText = await response.text();


    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlText, 'text/html');


    const banner = doc.querySelector('.imgContainer img').src;

    if (!banner) {
      console.warn('No banner element found in', url);
      return null;
    }


    return banner; 

  } catch (err) {
    console.error('Error fetching banner:', err);
  }
}


async function search(query) {
  let articles = await getArticlesPath();

  let results = articles.filter(article =>
    article.path.toLowerCase().includes(query.toLowerCase())
  );

  return results;
}

async function injectSearch() {
    let query = document.querySelector(".search input").value;

    let result = await search(query);

    injectArticles(result)
    injectTitle(`Resultados para ${query}`)
}

async function injectTitle(title) {
    innerTitle.innerText = title
}

async function importStatic() {

  fetch('/template/staticImports.html')
  .then(response => response.text())
  .then(html =>{
      head = document.querySelector("head")
      head.innerHTML += html
  })

}


function baixar(){
  let markdonw = document.querySelector(".markdown-body");
  
}