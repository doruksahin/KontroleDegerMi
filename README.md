# Kontrole Değer iddiaların Tespiti
### Detecting Check-Worty Claims
- Bu araştırma, verilen bir metnin kontrol edilmeye değer olup olmadığı bilgisini bulmak için yapılmış bir çalışmadır. 
- Günümüzde sosyal medya kullanımının yaygınlaşmasından ve yalan haberlerin artmasından dolayı ortaya atılan iddiaların teyiti gerekmekte ve teyit edilecek metinlerin doğru bir şekilde bulunması gerekmekte olduğundan dolayı, kontrole değer iddiaların tespiti araştırması yapılmıştır. Çalışmada Türkçe için optimize edilmiş doğal dil işleme yöntemleri, öznitelik olarak POS, NER, BOW ve cümle uzunluğu kullanılmış, bu özniteliklerin farklı kombinasyonları 2 farklı denetimli makine öğrenmesi algoritması ile test edilmiş ve sonuçları karşılaştırılmıştır. Böylece Türkçe dilindeki ilk kontrole değer iddiaların tespiti çalışması yapılmıştır. Sonucunda taban çizgimiz olan ClaimBuster araştırmasına yakın bir başarı Türkçe için elde edilmiştir.  
  
(Python version: 3)

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
- Bu komut ile tüm veriler bir araya getirilir. Dosya formatı argümanına göre json veya txt olarak kaydedilir. claims adında sonuçlar output klasörüne kaydedilir.


## Preprocessing ve Feature Extraction İşlemleri
#### Test Features
```
python main.py "preprocess" test_input.txt test_out.json 						  
python main.py "extract-feature" test_out.json test_feature_claim.csv  
python main.py "extract-feature" test_out.json test_feature_non_claim.csv  
```

#### Train Features
```
python main.py "preprocess" train_input.txt train_out.json 						
python main.py "extract-feature" train_out.json train_feature_claim.csv  
python main.py "extract-feature" train_out.json train_feature_non_claim.csv  
```
- train_input.txt claims.txt'den geliyor. Crawl edilen veriler iddia olarak, twitter API ile çekilen veriler iddia değil olarak varsayılmıştır.

#### Bayes Classifier
```
python bayes_classifier.py test_input.json test_feature.csv expected.json train_feature_claim.csv train_feature_not_claim.csv  
```

#### Baseline Karşılaştırması İçin Çeviri İşlemi
- mtranslate klasöründe aşağıdaki komut çalıştırıldığında <DOSYA_ADI>_translated.json şeklinde ingilizceye çevrilmiş formatta kaydediliyor. 
```
python main.py <DOSYA_ADI>
```

#### Baseline API (ClaimBuster)
```
python claimbuster_api.py <DOSYA_ADI> <CIKTI_ADI>  
python compare_baseline.py claimbuster_results.json expected.json
```
- İlk komut çalıştığında çıktı olarak \["metin", "is_checkworty"\] şeklinde json oluşmaktadır.
- İkinci komut claimbuster sonucunun etiketlenmiş veriler (expected.json) üzerinde başarısını bulmaktadır.


#### Etiketleme İşlemi
```
python split_files.py <DOSYA_ADI>  
python gui.py <DOSYA_ADI> 
```
- mark-nonworthy klasöründe ilk komut çalıştığında dosya "ali.json", "said.json", "doruk.json" olarak üçe bölünüyor.
- İkinci komut ile etiketleme arayüzü açılmaktadır.
- Etiketleme bittikten sonra kaydet tuşuna basılır ve dosya_adi_output.json şeklinde etiketlenmiş veri elde edilir.

#### Önceden Eğitilmiş Model Çalıştırma
- SVM (Length + POS + NER) modelini test etmek için:
```
python pretrained.py
```
