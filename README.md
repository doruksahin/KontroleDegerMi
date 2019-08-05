# Kontrole Değer iddiaların Tespiti
### Detecting Check-Worty Claims
- Bu araştırma, verilen bir metnin kontrol edilmeye değer olup olmadığı bilgisini bulmak için yapılmış bir çalışmadır. 
- Günümüzde sosyal medya kullanımının yaygınlaşmasından ve yalan haberlerin artmasından dolayı ortaya atılan iddiaların teyiti gerekmekte ve teyit edilecek metinlerin doğru bir şekilde bulunması gerekmekte olduğundan dolayı, kontrole değer iddiaların tespiti araştırması yapılmıştır. Çalışmada Türkçe için optimize edilmiş doğal dil işleme yöntemleri, öznitelik olarak POS, NER, BOW ve cümle uzunluğu kullanılmış, bu özniteliklerin farklı kombinasyonları 2 farklı denetimli makine öğrenmesi algoritması ile test edilmiş ve sonuçları karşılaştırılmıştır. Böylece Türkçe dilindeki ilk kontrole değer iddiaların tespiti çalışması yapılmıştır. Sonucunda taban çizgimiz olan ClaimBuster araştırmasına yakın bir başarı Türkçe için elde edilmiştir.


## Crawl İşlemi
```
python dogrulaorg.py  
python dogrulukpayi.py  
python gununyalanlari.py  
python malumatfurus.py  
python teyitorg.py
```
- Bu komutlar çalıştırıldığında crawl/output klasörüne çekilen veriler json formatında gelmektedir.
```
python arrange.py <DOSYA_FORMATI>  
```
- Bu komut ile tüm veriler bir araya getirilir. Dosya formatı argümanına göre json veya txt olarak kaydedilir.


- pipeline klasöründe preprocessing ve feature extraction için 
- == TEST FEATURELARI İÇİN ==  
- python main.py "preprocess" test_input.txt test_out.json 						  
- python main.py "extract-feature" test_out.json test_feature_claim.csv  
- python main.py "extract-feature" test_out.json test_feature_non_claim.csv  


- == TRAIN FEATURELARI İÇİN ==  
- python main.py "preprocess" train_input.txt train_out.json 						-> train_input.txt claims.txt'den geliyor.  
- python main.py "extract-feature" train_out.json train_feature_claim.csv  
- python main.py "extract-feature" train_out.json train_feature_non_claim.csv  


- Bayes classifier'a sokarak başarı oranımızı ekrana bastık.  
- == BAYES CLASSIFIER'A SOKMAK İÇİN ==  
- python bayes_classifier.py test_input.json test_feature.csv expected.json train_feature_claim.csv train_feature_non_claim.csv  


- ===== Baseline kontrolü =====  
- mtranslate klasöründe   
- python main.py <DOSYA_ADI> komutu çalıştırıldığında <DOSYA_ADI>_translated.json şeklinde ingilizceye çevrilmiş formata dönüştürülüyor.  
- Bu çıktıyı claimbuster klasörüne koyuyoruz.  
- claimbuster klasöründe  
-
- python claimbuster_api.py <DOSYA_ADI> <CIKTI_ADI>  
- çıktı formatı jsonlardan oluşmaktadır. bir json bloğunun içinde "tweet", "is_checkworthy" attributelari var.  
-
- python compare_baseline.py claimbuster_results.json expected.json komutu ile baseline başarı oranını ekrana bastık.  
- claimbuster_results.json'ı yukarıdaki claimbuster klasöründen elde ettik.  
- expected.json için işaretleme yaptık- 

- ====== İŞARETLEME İŞLEMİ ======  
- mark-nonworthy klasöründe  
- python split_files.py <DOSYA_ADI>   
- komutunu çalıştırdığımızda dosya "ali.json", "said.json", "doruk.json" şeklinde 3'e bölünüyor.  

- python gui.py <DOSYA_ADI>  
- komutu ile işaretleme arayüzüne giriyoruz ve işaretleme bitince kaydedip çıkıyoruz. Kaydedip çıkınca dosya_adi_output.json şeklinde bir çıktımız oluyor.  
