# CandyCrushDemo

Javascript, CSS ve HTML ile basit candy crush oyunu 

Oyunu oynamak için [tıklayınız](http://candycrushgame.eu5.org/).

![oyun görseli](https://github.com/zeynep-dmrl/CandyCrushDemo/blob/main/images/game_screenshot.png)

## Proje Detayı

Candy Crush oyun mantığıyla javascript css html kullanarak kolay bir oyun tasarladım.
Oyunun nasıl tasarlanıcağı kısaca anlatmak gerekirse;
Bir html ana sayfasında bir grid modülü tanımlıyoruz. Konumlandırma kullanmak zorunda kalmadan satırlar ve sütunlar içeren bir düzen sistemi sunar. 
javascript sayfasında bu etiketin içine div etiketleri yerleştiriyoruz. Bu şekilde oyun panosu oluşturuldu. Oyun panosu satır ve sütünlara bölünüp karelere 
rastgele sekerleri yerleştiriyoruz. Kareleri sürüklenebilir hareketli elemanlar haline getirip bu hareketlerin başlangıç bitiş yerlerini kontrol ediyoruz.
3 satır ve sutun , 4 satır ve sütün şeklinde şekerlerin eşleşmesini kontrol ediyoruz. Şekerlerin eşleşmesi ve yeni şekerlerin 
gelmesini sağladıktan sonra fonksiyonları çağırmamız yeterli.

### Fonksiyonlar
Kullanılan bazı javascript fonksiyonları

DOM (Document Object Module) HTML dökümanları içerisinde bulunan nesnelere kolaylıkla
erişim sağlamak ve üzerinde işlemler yapabilmek için tasarlanan bir modeldir. DOM ile
HTML dosyamızda bulunan her şeye erişim sağlayabiliriz.

addEventListener() , belirtilen ögeye bir olay işleyicisini ekler.Bu olay meydana 
geldiğinde dinleyici fonksiyon yürütülür.

setAttribute() , belirtilen özniteliği bir öğeye ekler ve ona belirtilen değeri verir.

setInterval() , bir işlevi çağırır veya belirli aralıklarla (milisaniye cinsinden) 
bir ifadeyi değerlendirir.

querySelector() , belgedeki belirtilen CSS seçicileriyle eşleşen ilk öğeyi döndürür.
tüm öğelere erişmek için querySelectorAll() yöntemi kullanılabilir.

Math.random() , rasgele 0'dan 1'e kadar sayı üretir.

createElement() , belirtilen ada sahip yeni bir HTML öğesi oluşturur.

appendChild() , belirtilen üst düğümün alt düğümlerinin sonuna bir düğüm ekler.

every() , verilen koşula bir dizi içerisindeki tüm elemenların uyup uymadığını 
kontrol eder.

forEach()

includes()

contains()

add()

remove()

push()
