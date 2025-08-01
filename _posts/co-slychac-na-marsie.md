## Co słychać na Marsie?

Programiści zmieniają świat. Ich praca jest niezbędna do eksploracji kosmosy. Spróbujmy i my :D

Jako że nam nie udało się jeszcze nikogo wysłać w kosmos skorzystamy z pomocy i zasobów NASA.

Najpierw musimy zdobyć klucz dostępu. Zrobimy to tu: [https://api.nasa.gov/index.html\#apply-for-an-api-key](https://api.nasa.gov/index.html#apply-for-an-api-key).

Pomoże nam on dostać się zasobów udostępnianych przez NASA. Ich listę możecie znaleźć tu: [https://api.nasa.gov/api.html\#how-do-i-see-my-current-usage?](https://api.nasa.gov/api.html#how-do-i-see-my-current-usage?)

Na początek zaczniemy od zdjęcia dnia :\)

Kiedy wejdziecie na ten adres [https://api.nasa.gov/planetary/apod?api\_key=DEMO\_KEY](https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY) zobaczycie... obiekt.

Mamy datę, opis, adresy do zdjęć w dwóch rozmiarach, typ oraz tytuł. Stworzymy stronę, której tłem będzie zdjęcie dnia. Sprawdźmy, jakie jest dzisiaj :D

Na początek pobierz paczkę z plikiem HTML, CSS i JS, które jest [TUTAJ](https://drive.google.com/open?id=1F6R627Cw6tPFS9K-6iqVS3eMNu4_1nlQ)

Zaczniemy od tego by zmieniać tło body na obraz. W CSSach służy do tego background-image. By zmienić tło za pomocą JSa stworzymy funkcję, której argumentem będzie ścieżka do obrazka:

```js
function changeBackground(imageURL) {

}
```

Posłużymy się właściwością style którą już znamy. Na liście wszystkich styli jest też backgroundImage. To mu przypiszemy adres do naszego obrazka.

Standardowo wyglądałoby to tak:

```js
document.body.style.backgroundImage = "url('img_unicorn.png')";
```

Ale nasz adres obrazka będzie się zmieniał i będzie przyjmował wartość, którą wpiszemy jako argument funkcji więc:

```js
function changeBackground(imageURL) {
    document.body.style.backgroundImage = "url('" + imageURL + "')";
}
```

Teraz czas na podłączenie się do api NASA!

Na początek stworzymy zmienną z adresem URL pod którym kryje się obiekt z naszym obrazkiem. Zamiast DEMO\_KEY wpisujemy nasz klucz.

```js
var dataURL = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY';
```

Teraz stwórzmy funkcję getPicture. W jej wnętrzu napiszemy kod który będzie pobierał dane z adresu wskazanego pod dataURL. Posłuży nam do tego fetch API - narzędzie do dynamicznego pobierania danych. Jest to dość nowe rozwiązanie, obsługiwane przez nowe przeglądarki.

Spróbujemy po kolei:

```js
function getPicture() {
    fetch(dataURL)
    .then((resp) => {
        console.log(resp);
    })
}
```

Po uruchemieniu fetch zwraca nam Promise. Promise'y pozwalają nam kontrolować kolejność kodu. Jeżeli jakaś obietnica została spełniona zaczyna działaś kolejny kawałek kodu \(then\). Jeśli pod adresem dataURL coś się znajduje uzyskujemy dostęp do odpowiedzi z tej strony i ją wyświetlamy.

Kolejny nowy elemeny to strzałki =&gt;. Jest to prostszy zapis znanych nam funkcji. Nasza funkcja ma jeden argument \(resp\) i ten argument wyświetla w konsoli. Wywołajmy funkcję i spójrzmy na naszą konsolę. Mamy w niej odpowiedź z serwera. Zamieńmy ją na przyjaźniejszy format, np. json. Najczęściej dane w formacie JSON są pobierane z serwera jako tekst, a następnie przekształcane w obiekt. By przekształcić naszą odpowiedź z serwera dopiszmy do niej metodę json\(\).

```js
function getPicture() {
    fetch(dataURL)
    .then((resp) => {
        return resp.json();
    })
}
```

To także jest obietnica \(Promise\). Bo jej spełnieniu powinniśmy móc wyświetlić nasz obiekt. Sprawdźmy

```js
function getPicture() {
    fetch(dataURL)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            console.log(data);
        });
}
```

Mamy nasz obiekt! Nam jednak zależy na konkretnym elemencie: hdurl. Pamiętasz jak w obiekcie wyświetlamy daną wartość? Dokładnie - odwołując się do klucza.

```js
function getPicture() {
    fetch(dataURL)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            console.log(data.hdurl);
        });
}
```

Jest i nasz url, który powinniśmy użyć jako argument w funkcji changeBackground:

```js
function getPicture() {
    fetch(dataURL)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            changeBackground(data.hdurl);
        });
}
```

Wiemy już jakie jest zdjęcie dnia?

### Na podbój Marsa!

Teraz zróbmy krok dalej. Sprawdźmy co słychać na Marsie. Pomoże nam w tym łazik który dzielnie fotografuje swoje dzienne przygody, a dane z tych wypraw znajdziecie pod [https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api\_key=DEMO\_\_KEY](https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO__KEY)

Zacznijmy od przypisania naszego URLa do zmiennej:

```js
var urlMars = https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&apikey=DEMO_KEY
```

stwórzmy nową funkcję która będzie korzystała ze znanego nam narzedzia fetch API:

```js
function getMarsPicture() {
    fetch(urlMars)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            console.log(data);
        });
}
```

Wywołajmy funkcję i sprawdźmy, co dzieje się w konsoli. Mamy obiekt z kluczem photos. Sprawdźmy co jest w środku:

```js
function getMarsPicture() {
    fetch(urlMars)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            console.log(data.photos);
        });
}
```

W środku mamy tablicę obiektów. Sprawdźmy ile jest obiektów:

```js
function getMarsPicture() {
    fetch(urlMars)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            console.log(data.photos.length);
        });
}
```

Bardzo dużo. Sprawdźmy co jest w środku, np. w pierwszym z nich:

```js
function getMarsPicture() {
    fetch(urlMars)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            console.log(data.photos[0]);
        });
}
```

To już jest bliższe naszym oczekiwaniom. Mamy obiekt, w środku jest klucz img\_src z adresem naszego obrazka. Zróbmy na naszej stronie galerię. Będzie się ona znajdować w divie o id content. Stwórzmy więc zmienna:

```js
var gallery = document.getElementById('content');
```

Teraz stwórzmy funkcję creteGallery z argumentem dataList. Będzie to właśnie lista ta bardzo dług tablica która wyciągneliśmy z data.photos :

```js
function createGallery(dataList) {
}
```

Wewnątrz funkcji za pomocą pętli stworzymy 9 obrazków i dodamy go do strony. W HTML obraz wyświetlama za pomocą taga img:

```markdown
<img src="adres_obrazka" class="klasa/klasy" alt="co_sie_wyswietli_jesli pod danym adresem nie ma obrazka">
```

Tak będzie on wyglądać w HTML a jak to zrobić za pomocą JS? Zacznijmy od pętli która będzie się powtarzać 9 razy:

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {

    }
}
```

Za każdym razem będziemy tworzyć nowy element. Będziemy go przypisywać do zmiennej img. Nowy element tworzymy za pomocą:

```js
document.createElement('nazwa_tagu');
```

U nas nazwą tagu będzie img, czyli:

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {
        var img = document.createElement('img');
    }
}
```

Kolejny krok to wstawienie nowego  elementu do diva content. Służy do tego metoda appendChild\('nazwa\__wstawianego\_elementu_'\):

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {
        var img = document.createElement('img');
        gallery.appendChild(img);
    }
}
```

Sprawdźmy naszą stronę.

Brakuje naszych ścieżek do obrazków. Wróćmy do funkcji getMarsPictures. Mieliśmy tu tablicę z wieloma obiektami w środku których mieliśmy potrzebny nam img\_src. Przypiszmy naszą tablicę do zmiennej:

```js
function getMarsPicture() {
    fetch(urlMars)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            pictureList = data.photos;
        });
}
```

Mamy tu listę którą będziemy wykorzystywać w funkcji createGallery. Wywołajmy więc createGallery z tym argumentem wewnątrz funckji getMarsPicture:

```js
function getMarsPicture() {
    fetch(urlMars)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            pictureList = data.photos;
            createGallery(pictureList);
        });
}
```

Ok, ale co się ktyje pod naszym pistureList. Sprawdźmy to za pomocą console.log. W funkcji createGallery wyświetlmy w konsoli nasz argument dataList. Teraz wywołajmy funkcję getMarsPicture. W niej wywołujemy też funkcję createGallery:

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {
        var img = document.createElement('img');
        gallery.appendChild(img);
        console.log(dataList);
    }
}
```

Mamy 9 tablic, w których są nasze obiekty. A my przy każdej pętli potrzebujemy tylko 1 obiekt. Obiekt którego index jest zgodny z naszym i, dlatego wyświetlajmy tylko obiekty o indexie równym i:

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {
        var img = document.createElement('img');
        gallery.appendChild(img);
        console.log(dataList[i]);
    }
}
```

Jesteśmy bliżej - mamy 9 obiektów. A potrzebujemy tylko wartość która kryje się pod img\_src, więc wyświetlmy ją:

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {
        var img = document.createElement('img');
        gallery.appendChild(img);
        console.log(dataList[i].img_src);
    }
}
```

Coraz lepiej. Teraz zmiast ją wyświetlać przypiszmy ją do zmiennej i przesuńmy przed dodanie img do gallery:

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {
        var img = document.createElement('img');
        var imgPath = dataList[i].img_src;
        gallery.appendChild(img);
    }
}
```

Jak teraz dodać imgPath do naszego elementu img? Za pomocą właściwości src. Jest podobna do właściwości style. Musimy jej przypisać wartość:

```js
function createGallery(dataList) {
    for(var i=0; i < 9; i++) {
        var img = document.createElement('img');
        var imgPath = dataList[i].img_src;
        img.src = imgPath;
        gallery.appendChild(img);
    }
}
```

Sprawdźmy co słychać na Marsie!

