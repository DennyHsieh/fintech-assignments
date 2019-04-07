## About zh-NER-TF training
- Training log is shown as below.

```
$ python main.py --mode=train
/home/denny/anaconda3/lib/python3.6/site-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
vocab_size: 3905
Namespace(CRF=True, batch_size=64, clip=5.0, demo_model='1521112368', dropout=0.5, embedding_dim=300, epoch=40, hidden_dim=300, lr=0.001, mode='train', optimizer='Adam', pretrain_embedding='random', shuffle=True, test_data='data_path', train_data='data_path', update_embedding=True)
WARNING:tensorflow:From /home/denny/anaconda3/lib/python3.6/site-packages/tensorflow/python/ops/rnn.py:417: calling reverse_sequence (from tensorflow.python.ops.array_ops) with seq_dim is deprecated and will be removed in a future version.
Instructions for updating:
seq_dim is deprecated, use seq_axis instead
From /home/denny/anaconda3/lib/python3.6/site-packages/tensorflow/python/ops/rnn.py:417: calling reverse_sequence (from tensorflow.python.ops.array_ops) with seq_dim is deprecated and will be removed in a future version.
Instructions for updating:
seq_dim is deprecated, use seq_axis instead
WARNING:tensorflow:From /home/denny/anaconda3/lib/python3.6/site-packages/tensorflow/python/util/deprecation.py:432: calling reverse_sequence (from tensorflow.python.ops.array_ops) with batch_dim is deprecated and will be removed in a future version.
Instructions for updating:
batch_dim is deprecated, use batch_axis instead
From /home/denny/anaconda3/lib/python3.6/site-packages/tensorflow/python/util/deprecation.py:432: calling reverse_sequence (from tensorflow.python.ops.array_ops) with batch_dim is deprecated and will be removed in a future version.
Instructions for updating:
batch_dim is deprecated, use batch_axis instead
/home/denny/anaconda3/lib/python3.6/site-packages/tensorflow/python/ops/gradients_impl.py:100: UserWarning: Converting sparse IndexedSlices to a dense Tensor of unknown shape. This may consume a large amount of memory.
  "Converting sparse IndexedSlices to a dense Tensor of unknown shape. "
train data: 50658
2019-04-05 23:15:10 epoch 1, step 1, loss: 73.13, global_step: 1
2019-04-05 23:15:10 epoch 1, step 300, loss: 8.149, global_step: 300
2019-04-05 23:15:10 epoch 1, step 600, loss: 5.766, global_step: 600
2019-04-05 23:15:10 epoch 1, step 792, loss: 4.675, global_step: 792
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5986 phrases; correct: 4000.
accuracy:  96.42%; precision:  66.82%; recall:  64.60%; FB1:  65.69
LOC: precision:  68.35%; recall:  68.02%; FB1:  68.19  2863
ORG: precision:  57.32%; recall:  52.67%; FB1:  54.89  1223
PER: precision:  70.63%; recall:  67.64%; FB1:  69.10  1900
2019-04-05 23:35:10 epoch 2, step 1, loss: 2.693, global_step: 793
2019-04-05 23:35:10 epoch 2, step 300, loss: 3.247, global_step: 1092
2019-04-05 23:35:10 epoch 2, step 600, loss: 2.43, global_step: 1392
2019-04-05 23:35:10 epoch 2, step 792, loss: 2.895, global_step: 1584
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5887 phrases; correct: 4632.
accuracy:  97.28%; precision:  78.68%; recall:  74.81%; FB1:  76.70
LOC: precision:  82.02%; recall:  78.00%; FB1:  79.96  2736
ORG: precision:  69.40%; recall:  67.47%; FB1:  68.42  1294
PER: precision:  80.24%; recall:  75.10%; FB1:  77.58  1857
2019-04-05 23:55:05 epoch 3, step 1, loss: 2.196, global_step: 1585
2019-04-05 23:55:05 epoch 3, step 300, loss: 2.296, global_step: 1884
2019-04-05 23:55:05 epoch 3, step 600, loss: 1.71, global_step: 2184
2019-04-05 23:55:05 epoch 3, step 792, loss: 1.736, global_step: 2376
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5797 phrases; correct: 4799.
accuracy:  97.53%; precision:  82.78%; recall:  77.50%; FB1:  80.06
LOC: precision:  84.91%; recall:  79.39%; FB1:  82.05  2690
ORG: precision:  75.85%; recall:  71.98%; FB1:  73.86  1263
PER: precision:  84.44%; recall:  78.48%; FB1:  81.35  1844
2019-04-06 00:14:01 epoch 4, step 1, loss: 2.005, global_step: 2377
2019-04-06 00:14:01 epoch 4, step 300, loss: 1.643, global_step: 2676
2019-04-06 00:14:01 epoch 4, step 600, loss: 1.773, global_step: 2976
2019-04-06 00:14:01 epoch 4, step 792, loss: 1.886, global_step: 3168
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5846 phrases; correct: 5010.
accuracy:  97.86%; precision:  85.70%; recall:  80.91%; FB1:  83.24
LOC: precision:  87.50%; recall:  82.76%; FB1:  85.07  2721
ORG: precision:  82.05%; recall:  73.85%; FB1:  77.74  1198
PER: precision:  85.42%; recall:  82.96%; FB1:  84.17  1927
2019-04-06 00:33:06 epoch 5, step 1, loss: 1.684, global_step: 3169
2019-04-06 00:33:06 epoch 5, step 300, loss: 1.304, global_step: 3468
2019-04-06 00:33:06 epoch 5, step 600, loss: 1.016, global_step: 3768
2019-04-06 00:33:06 epoch 5, step 792, loss: 1.382, global_step: 3960
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5898 phrases; correct: 5089.
accuracy:  97.92%; precision:  86.28%; recall:  82.19%; FB1:  84.19
LOC: precision:  88.32%; recall:  83.87%; FB1:  86.04  2732
ORG: precision:  81.29%; recall:  77.39%; FB1:  79.29  1267
PER: precision:  86.68%; recall:  82.96%; FB1:  84.78  1899
2019-04-06 00:51:57 epoch 6, step 1, loss: 0.7817, global_step: 3961
2019-04-06 00:51:57 epoch 6, step 300, loss: 1.144, global_step: 4260
2019-04-06 00:51:57 epoch 6, step 600, loss: 0.6516, global_step: 4560
2019-04-06 00:51:57 epoch 6, step 792, loss: 1.044, global_step: 4752
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5915 phrases; correct: 5164.
accuracy:  98.15%; precision:  87.30%; recall:  83.40%; FB1:  85.31
LOC: precision:  89.20%; recall:  87.24%; FB1:  88.21  2814
ORG: precision:  83.25%; recall:  78.06%; FB1:  80.57  1248
PER: precision:  87.16%; recall:  81.40%; FB1:  84.18  1853
2019-04-06 01:10:51 epoch 7, step 1, loss: 0.5497, global_step: 4753
2019-04-06 01:10:51 epoch 7, step 300, loss: 0.7432, global_step: 5052
2019-04-06 01:10:51 epoch 7, step 600, loss: 0.8875, global_step: 5352
2019-04-06 01:10:51 epoch 7, step 792, loss: 0.6067, global_step: 5544
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5926 phrases; correct: 5153.
accuracy:  98.16%; precision:  86.96%; recall:  83.22%; FB1:  85.05
LOC: precision:  89.94%; recall:  87.94%; FB1:  88.93  2813
ORG: precision:  81.96%; recall:  80.24%; FB1:  81.09  1303
PER: precision:  85.91%; recall:  78.38%; FB1:  81.97  1810
2019-04-06 01:29:38 epoch 8, step 1, loss: 0.5134, global_step: 5545
2019-04-06 01:29:38 epoch 8, step 300, loss: 1.155, global_step: 5844
2019-04-06 01:29:38 epoch 8, step 600, loss: 0.5345, global_step: 6144
2019-04-06 01:29:38 epoch 8, step 792, loss: 0.2127, global_step: 6336
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5995 phrases; correct: 5224.
accuracy:  98.21%; precision:  87.14%; recall:  84.37%; FB1:  85.73
LOC: precision:  90.60%; recall:  88.08%; FB1:  89.32  2797
ORG: precision:  81.40%; recall:  81.22%; FB1:  81.31  1328
PER: precision:  86.04%; recall:  81.10%; FB1:  83.50  1870
2019-04-06 01:48:31 epoch 9, step 1, loss: 0.557, global_step: 6337
2019-04-06 01:48:31 epoch 9, step 300, loss: 0.5734, global_step: 6636
2019-04-06 01:48:31 epoch 9, step 600, loss: 0.7665, global_step: 6936
2019-04-06 01:48:31 epoch 9, step 792, loss: 0.4543, global_step: 7128
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5932 phrases; correct: 5238.
accuracy:  98.22%; precision:  88.30%; recall:  84.59%; FB1:  86.41
LOC: precision:  91.46%; recall:  88.25%; FB1:  89.83  2776
ORG: precision:  83.63%; recall:  80.24%; FB1:  81.90  1277
PER: precision:  86.80%; recall:  82.21%; FB1:  84.44  1879
2019-04-06 02:07:21 epoch 10, step 1, loss: 0.9331, global_step: 7129
2019-04-06 02:07:21 epoch 10, step 300, loss: 0.4178, global_step: 7428
2019-04-06 02:07:21 epoch 10, step 600, loss: 0.2257, global_step: 7728
2019-04-06 02:07:21 epoch 10, step 792, loss: 0.3376, global_step: 7920
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5954 phrases; correct: 5251.
accuracy:  98.22%; precision:  88.19%; recall:  84.80%; FB1:  86.46
LOC: precision:  91.47%; recall:  89.09%; FB1:  90.26  2802
ORG: precision:  82.08%; recall:  82.57%; FB1:  82.32  1339
PER: precision:  87.64%; recall:  80.09%; FB1:  83.70  1813
2019-04-06 02:26:13 epoch 11, step 1, loss: 0.5097, global_step: 7921
2019-04-06 02:26:13 epoch 11, step 300, loss: 0.5711, global_step: 8220
2019-04-06 02:26:13 epoch 11, step 600, loss: 0.3425, global_step: 8520
2019-04-06 02:26:13 epoch 11, step 792, loss: 0.3999, global_step: 8712
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5967 phrases; correct: 5292.
accuracy:  98.31%; precision:  88.69%; recall:  85.47%; FB1:  87.05
LOC: precision:  92.63%; recall:  87.83%; FB1:  90.17  2728
ORG: precision:  81.44%; recall:  84.37%; FB1:  82.88  1379
PER: precision:  88.28%; recall:  82.76%; FB1:  85.43  1860
2019-04-06 02:45:05 epoch 12, step 1, loss: 0.3562, global_step: 8713
2019-04-06 02:45:05 epoch 12, step 300, loss: 0.3369, global_step: 9012
2019-04-06 02:45:05 epoch 12, step 600, loss: 0.4248, global_step: 9312
2019-04-06 02:45:05 epoch 12, step 792, loss: 0.431, global_step: 9504
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6049 phrases; correct: 5354.
accuracy:  98.38%; precision:  88.51%; recall:  86.47%; FB1:  87.48
LOC: precision:  91.65%; recall:  89.26%; FB1:  90.44  2802
ORG: precision:  85.05%; recall:  83.77%; FB1:  84.41  1311
PER: precision:  86.31%; recall:  84.22%; FB1:  85.26  1936
2019-04-06 03:03:55 epoch 13, step 1, loss: 0.2547, global_step: 9505
2019-04-06 03:03:55 epoch 13, step 300, loss: 0.4567, global_step: 9804
2019-04-06 03:03:55 epoch 13, step 600, loss: 0.189, global_step: 10104
2019-04-06 03:03:55 epoch 13, step 792, loss: 0.5462, global_step: 10296
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6043 phrases; correct: 5384.
accuracy:  98.41%; precision:  89.09%; recall:  86.95%; FB1:  88.01
LOC: precision:  92.44%; recall:  89.26%; FB1:  90.82  2778
ORG: precision:  84.34%; recall:  82.57%; FB1:  83.45  1303
PER: precision:  87.51%; recall:  86.54%; FB1:  87.02  1962
2019-04-06 03:22:44 epoch 14, step 1, loss: 0.313, global_step: 10297
2019-04-06 03:22:44 epoch 14, step 300, loss: 0.304, global_step: 10596
2019-04-06 03:22:44 epoch 14, step 600, loss: 0.1681, global_step: 10896
2019-04-06 03:22:44 epoch 14, step 792, loss: 0.5469, global_step: 11088
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5996 phrases; correct: 5352.
accuracy:  98.43%; precision:  89.26%; recall:  86.43%; FB1:  87.82
LOC: precision:  92.09%; recall:  89.82%; FB1:  90.94  2806
ORG: precision:  84.39%; recall:  84.07%; FB1:  84.23  1326
PER: precision:  88.47%; recall:  83.11%; FB1:  85.71  1864
2019-04-06 03:41:33 epoch 15, step 1, loss: 0.1204, global_step: 11089
2019-04-06 03:41:33 epoch 15, step 300, loss: 0.2305, global_step: 11388
2019-04-06 03:41:33 epoch 15, step 600, loss: 0.5509, global_step: 11688
2019-04-06 03:41:33 epoch 15, step 792, loss: 0.04901, global_step: 11880
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5963 phrases; correct: 5340.
accuracy:  98.37%; precision:  89.55%; recall:  86.24%; FB1:  87.87
LOC: precision:  92.14%; recall:  88.43%; FB1:  90.24  2761
ORG: precision:  85.47%; recall:  82.64%; FB1:  84.03  1287
PER: precision:  88.56%; recall:  85.48%; FB1:  87.00  1915
2019-04-06 04:00:27 epoch 16, step 1, loss: 0.2922, global_step: 11881
2019-04-06 04:00:27 epoch 16, step 300, loss: 0.4263, global_step: 12180
2019-04-06 04:00:27 epoch 16, step 600, loss: 0.05637, global_step: 12480
2019-04-06 04:00:27 epoch 16, step 792, loss: 0.2409, global_step: 12672
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5931 phrases; correct: 5318.
accuracy:  98.41%; precision:  89.66%; recall:  85.89%; FB1:  87.73
LOC: precision:  92.73%; recall:  88.18%; FB1:  90.40  2736
ORG: precision:  86.17%; recall:  82.42%; FB1:  84.25  1273
PER: precision:  87.62%; recall:  84.88%; FB1:  86.23  1922
2019-04-06 04:19:16 epoch 17, step 1, loss: 0.07223, global_step: 12673
2019-04-06 04:19:16 epoch 17, step 300, loss: 0.1943, global_step: 12972
2019-04-06 04:19:16 epoch 17, step 600, loss: 0.3636, global_step: 13272
2019-04-06 04:19:16 epoch 17, step 792, loss: 0.2219, global_step: 13464
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6060 phrases; correct: 5402.
accuracy:  98.48%; precision:  89.14%; recall:  87.24%; FB1:  88.18
LOC: precision:  92.86%; recall:  89.09%; FB1:  90.93  2760
ORG: precision:  85.10%; recall:  84.07%; FB1:  84.58  1315
PER: precision:  86.65%; recall:  86.69%; FB1:  86.67  1985
2019-04-06 04:38:06 epoch 18, step 1, loss: 0.3919, global_step: 13465
2019-04-06 04:38:06 epoch 18, step 300, loss: 0.1022, global_step: 13764
2019-04-06 04:38:06 epoch 18, step 600, loss: 0.2989, global_step: 14064
2019-04-06 04:38:06 epoch 18, step 792, loss: 0.3426, global_step: 14256
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6010 phrases; correct: 5372.
accuracy:  98.51%; precision:  89.38%; recall:  86.76%; FB1:  88.05
LOC: precision:  93.10%; recall:  89.54%; FB1:  91.28  2767
ORG: precision:  84.71%; recall:  84.52%; FB1:  84.62  1328
PER: precision:  87.26%; recall:  84.22%; FB1:  85.71  1915
2019-04-06 04:56:51 epoch 19, step 1, loss: 0.07801, global_step: 14257
2019-04-06 04:56:51 epoch 19, step 300, loss: 0.102, global_step: 14556
2019-04-06 04:56:51 epoch 19, step 600, loss: 0.1832, global_step: 14856
2019-04-06 04:56:51 epoch 19, step 792, loss: 0.1655, global_step: 15048
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5997 phrases; correct: 5315.
accuracy:  98.40%; precision:  88.63%; recall:  85.84%; FB1:  87.21
LOC: precision:  91.39%; recall:  90.34%; FB1:  90.86  2844
ORG: precision:  83.91%; recall:  84.22%; FB1:  84.06  1336
PER: precision:  87.78%; recall:  80.39%; FB1:  83.93  1817
2019-04-06 05:15:43 epoch 20, step 1, loss: 0.06921, global_step: 15049
2019-04-06 05:15:43 epoch 20, step 300, loss: 0.317, global_step: 15348
2019-04-06 05:15:43 epoch 20, step 600, loss: 0.1818, global_step: 15648
2019-04-06 05:15:43 epoch 20, step 792, loss: 0.1334, global_step: 15840
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5984 phrases; correct: 5361.
accuracy:  98.44%; precision:  89.59%; recall:  86.58%; FB1:  88.06
LOC: precision:  93.70%; recall:  88.91%; FB1:  91.24  2730
ORG: precision:  84.11%; recall:  83.55%; FB1:  83.83  1322
PER: precision:  87.53%; recall:  85.23%; FB1:  86.36  1932
2019-04-06 05:34:39 epoch 21, step 1, loss: 0.3757, global_step: 15841
2019-04-06 05:34:39 epoch 21, step 300, loss: 0.1453, global_step: 16140
2019-04-06 05:34:39 epoch 21, step 600, loss: 0.2518, global_step: 16440
2019-04-06 05:34:39 epoch 21, step 792, loss: 0.1758, global_step: 16632
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6029 phrases; correct: 5393.
accuracy:  98.43%; precision:  89.45%; recall:  87.10%; FB1:  88.26
LOC: precision:  93.91%; recall:  89.05%; FB1:  91.42  2728
ORG: precision:  83.84%; recall:  84.22%; FB1:  84.03  1337
PER: precision:  87.07%; recall:  86.19%; FB1:  86.63  1964
2019-04-06 05:53:26 epoch 22, step 1, loss: 0.1051, global_step: 16633
2019-04-06 05:53:26 epoch 22, step 300, loss: 0.2135, global_step: 16932
2019-04-06 05:53:26 epoch 22, step 600, loss: 0.02993, global_step: 17232
2019-04-06 05:53:26 epoch 22, step 792, loss: 0.4419, global_step: 17424
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6133 phrases; correct: 5408.
accuracy:  98.44%; precision:  88.18%; recall:  87.34%; FB1:  87.76
LOC: precision:  91.85%; recall:  90.48%; FB1:  91.16  2834
ORG: precision:  84.17%; recall:  83.10%; FB1:  83.63  1314
PER: precision:  85.59%; recall:  85.64%; FB1:  85.61  1985
2019-04-06 06:12:20 epoch 23, step 1, loss: 0.2718, global_step: 17425
2019-04-06 06:12:20 epoch 23, step 300, loss: 0.1763, global_step: 17724
2019-04-06 06:12:20 epoch 23, step 600, loss: 0.2373, global_step: 18024
2019-04-06 06:12:20 epoch 23, step 792, loss: 0.08479, global_step: 18216
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6049 phrases; correct: 5422.
accuracy:  98.51%; precision:  89.63%; recall:  87.56%; FB1:  88.59
LOC: precision:  93.03%; recall:  89.54%; FB1:  91.25  2769
ORG: precision:  84.89%; recall:  84.45%; FB1:  84.67  1324
PER: precision:  88.04%; recall:  86.79%; FB1:  87.41  1956
2019-04-06 06:31:09 epoch 24, step 1, loss: 0.1172, global_step: 18217
2019-04-06 06:31:09 epoch 24, step 300, loss: 0.2119, global_step: 18516
2019-04-06 06:31:09 epoch 24, step 600, loss: 0.09898, global_step: 18816
2019-04-06 06:31:09 epoch 24, step 792, loss: 0.09545, global_step: 19008
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6020 phrases; correct: 5410.
accuracy:  98.52%; precision:  89.87%; recall:  87.37%; FB1:  88.60
LOC: precision:  93.46%; recall:  88.84%; FB1:  91.09  2735
ORG: precision:  85.37%; recall:  85.50%; FB1:  85.44  1333
PER: precision:  87.91%; recall:  86.49%; FB1:  87.20  1952
2019-04-06 06:49:58 epoch 25, step 1, loss: 0.2204, global_step: 19009
2019-04-06 06:49:58 epoch 25, step 300, loss: 0.06416, global_step: 19308
2019-04-06 06:49:58 epoch 25, step 600, loss: 0.2764, global_step: 19608
2019-04-06 06:49:58 epoch 25, step 792, loss: 0.2596, global_step: 19800
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6073 phrases; correct: 5414.
accuracy:  98.51%; precision:  89.15%; recall:  87.44%; FB1:  88.28
LOC: precision:  92.11%; recall:  89.64%; FB1:  90.86  2800
ORG: precision:  85.36%; recall:  84.97%; FB1:  85.17  1325
PER: precision:  87.47%; recall:  85.89%; FB1:  86.67  1948
2019-04-06 07:08:49 epoch 26, step 1, loss: 0.1056, global_step: 19801
2019-04-06 07:08:49 epoch 26, step 300, loss: 0.2201, global_step: 20100
2019-04-06 07:08:49 epoch 26, step 600, loss: 0.07764, global_step: 20400
2019-04-06 07:08:49 epoch 26, step 792, loss: 0.2312, global_step: 20592
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6053 phrases; correct: 5393.
accuracy:  98.44%; precision:  89.10%; recall:  87.10%; FB1:  88.08
LOC: precision:  93.02%; recall:  88.91%; FB1:  90.92  2750
ORG: precision:  83.37%; recall:  84.37%; FB1:  83.87  1347
PER: precision:  87.53%; recall:  86.29%; FB1:  86.90  1956
2019-04-06 07:27:36 epoch 27, step 1, loss: 0.0889, global_step: 20593
2019-04-06 07:27:36 epoch 27, step 300, loss: 0.09522, global_step: 20892
2019-04-06 07:27:36 epoch 27, step 600, loss: 0.1136, global_step: 21192
2019-04-06 07:27:36 epoch 27, step 792, loss: 0.1076, global_step: 21384
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6047 phrases; correct: 5412.
accuracy:  98.46%; precision:  89.50%; recall:  87.40%; FB1:  88.44
LOC: precision:  93.54%; recall:  89.16%; FB1:  91.30  2742
ORG: precision:  82.15%; recall:  85.73%; FB1:  83.90  1389
PER: precision:  89.04%; recall:  85.99%; FB1:  87.49  1916
2019-04-06 07:46:24 epoch 28, step 1, loss: 0.08803, global_step: 21385
2019-04-06 07:46:24 epoch 28, step 300, loss: 0.1741, global_step: 21684
2019-04-06 07:46:24 epoch 28, step 600, loss: 0.2817, global_step: 21984
2019-04-06 07:46:24 epoch 28, step 792, loss: 0.2805, global_step: 22176
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5966 phrases; correct: 5347.
accuracy:  98.47%; precision:  89.62%; recall:  86.35%; FB1:  87.96
LOC: precision:  93.75%; recall:  88.63%; FB1:  91.12  2720
ORG: precision:  82.97%; recall:  85.65%; FB1:  84.29  1374
PER: precision:  88.51%; recall:  83.52%; FB1:  85.94  1872
2019-04-06 08:05:10 epoch 29, step 1, loss: 0.2254, global_step: 22177
2019-04-06 08:05:10 epoch 29, step 300, loss: 0.05802, global_step: 22476
2019-04-06 08:05:10 epoch 29, step 600, loss: 0.2884, global_step: 22776
2019-04-06 08:05:10 epoch 29, step 792, loss: 0.1904, global_step: 22968
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6010 phrases; correct: 5375.
accuracy:  98.52%; precision:  89.43%; recall:  86.81%; FB1:  88.10
LOC: precision:  93.11%; recall:  90.16%; FB1:  91.61  2786
ORG: precision:  84.68%; recall:  84.75%; FB1:  84.72  1332
PER: precision:  87.37%; recall:  83.32%; FB1:  85.29  1892
2019-04-06 08:23:57 epoch 30, step 1, loss: 0.0876, global_step: 22969
2019-04-06 08:23:57 epoch 30, step 300, loss: 0.08699, global_step: 23268
2019-04-06 08:23:57 epoch 30, step 600, loss: 0.1346, global_step: 23568
2019-04-06 08:23:57 epoch 30, step 792, loss: 0.1229, global_step: 23760
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5984 phrases; correct: 5360.
accuracy:  98.43%; precision:  89.57%; recall:  86.56%; FB1:  88.04
LOC: precision:  93.58%; recall:  89.75%; FB1:  91.63  2759
ORG: precision:  84.62%; recall:  83.92%; FB1:  84.27  1320
PER: precision:  87.19%; recall:  83.72%; FB1:  85.42  1905
2019-04-06 08:42:48 epoch 31, step 1, loss: 0.2178, global_step: 23761
2019-04-06 08:42:48 epoch 31, step 300, loss: 0.1163, global_step: 24060
2019-04-06 08:42:48 epoch 31, step 600, loss: 0.1199, global_step: 24360
2019-04-06 08:42:48 epoch 31, step 792, loss: 0.357, global_step: 24552
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6039 phrases; correct: 5399.
accuracy:  98.52%; precision:  89.40%; recall:  87.19%; FB1:  88.28
LOC: precision:  93.17%; recall:  90.06%; FB1:  91.59  2781
ORG: precision:  84.50%; recall:  85.57%; FB1:  85.03  1348
PER: precision:  87.38%; recall:  84.12%; FB1:  85.72  1910
2019-04-06 09:01:33 epoch 32, step 1, loss: 0.1464, global_step: 24553
2019-04-06 09:01:33 epoch 32, step 300, loss: 0.08209, global_step: 24852
2019-04-06 09:01:33 epoch 32, step 600, loss: 0.257, global_step: 25152
2019-04-06 09:01:33 epoch 32, step 792, loss: 0.04545, global_step: 25344
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5972 phrases; correct: 5353.
accuracy:  98.50%; precision:  89.63%; recall:  86.45%; FB1:  88.01
LOC: precision:  93.06%; recall:  89.54%; FB1:  91.27  2768
ORG: precision:  84.08%; recall:  84.90%; FB1:  84.49  1344
PER: precision:  88.55%; recall:  83.01%; FB1:  85.69  1860
2019-04-06 09:20:25 epoch 33, step 1, loss: 0.08666, global_step: 25345
2019-04-06 09:20:25 epoch 33, step 300, loss: 0.1757, global_step: 25644
2019-04-06 09:20:25 epoch 33, step 600, loss: 0.09377, global_step: 25944
2019-04-06 09:20:25 epoch 33, step 792, loss: 0.008047, global_step: 26136
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5935 phrases; correct: 5345.
accuracy:  98.48%; precision:  90.06%; recall:  86.32%; FB1:  88.15
LOC: precision:  94.24%; recall:  89.22%; FB1:  91.66  2724
ORG: precision:  84.95%; recall:  84.00%; FB1:  84.47  1316
PER: precision:  87.60%; recall:  83.67%; FB1:  85.59  1895
2019-04-06 09:39:16 epoch 34, step 1, loss: 0.05218, global_step: 26137
2019-04-06 09:39:16 epoch 34, step 300, loss: 0.2132, global_step: 26436
2019-04-06 09:39:16 epoch 34, step 600, loss: 0.06245, global_step: 26736
2019-04-06 09:39:16 epoch 34, step 792, loss: 0.09977, global_step: 26928
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5971 phrases; correct: 5393.
accuracy:  98.54%; precision:  90.32%; recall:  87.10%; FB1:  88.68
LOC: precision:  93.12%; recall:  90.37%; FB1:  91.73  2792
ORG: precision:  86.71%; recall:  83.85%; FB1:  85.26  1287
PER: precision:  88.64%; recall:  84.53%; FB1:  86.53  1892
2019-04-06 09:58:06 epoch 35, step 1, loss: 0.09465, global_step: 26929
2019-04-06 09:58:06 epoch 35, step 300, loss: 0.1873, global_step: 27228
2019-04-06 09:58:06 epoch 35, step 600, loss: 0.226, global_step: 27528
2019-04-06 09:58:06 epoch 35, step 792, loss: 0.3283, global_step: 27720
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5996 phrases; correct: 5401.
accuracy:  98.56%; precision:  90.08%; recall:  87.23%; FB1:  88.63
LOC: precision:  93.61%; recall:  89.64%; FB1:  91.58  2755
ORG: precision:  85.29%; recall:  84.97%; FB1:  85.13  1326
PER: precision:  88.30%; recall:  85.23%; FB1:  86.74  1915
2019-04-06 10:16:54 epoch 36, step 1, loss: 0.05508, global_step: 27721
2019-04-06 10:16:54 epoch 36, step 300, loss: 0.1632, global_step: 28020
2019-04-06 10:16:54 epoch 36, step 600, loss: 0.1543, global_step: 28320
2019-04-06 10:16:54 epoch 36, step 792, loss: 0.05583, global_step: 28512
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6039 phrases; correct: 5440.
accuracy:  98.55%; precision:  90.08%; recall:  87.86%; FB1:  88.95
LOC: precision:  93.11%; recall:  90.23%; FB1:  91.65  2788
ORG: precision:  84.87%; recall:  86.40%; FB1:  85.63  1355
PER: precision:  89.35%; recall:  85.38%; FB1:  87.32  1896
2019-04-06 10:35:48 epoch 37, step 1, loss: 0.0888, global_step: 28513
2019-04-06 10:35:48 epoch 37, step 300, loss: 0.1371, global_step: 28812
2019-04-06 10:35:48 epoch 37, step 600, loss: 0.02189, global_step: 29112
2019-04-06 10:35:48 epoch 37, step 792, loss: 0.02257, global_step: 29304
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6012 phrases; correct: 5397.
accuracy:  98.51%; precision:  89.77%; recall:  87.16%; FB1:  88.45
LOC: precision:  93.36%; recall:  89.02%; FB1:  91.14  2743
ORG: precision:  83.62%; recall:  85.12%; FB1:  84.36  1355
PER: precision:  88.98%; recall:  85.84%; FB1:  87.38  1914
2019-04-06 10:55:08 epoch 38, step 1, loss: 0.02276, global_step: 29305
2019-04-06 10:55:08 epoch 38, step 300, loss: 0.1285, global_step: 29604
2019-04-06 10:55:08 epoch 38, step 600, loss: 0.295, global_step: 29904
2019-04-06 10:55:08 epoch 38, step 792, loss: 0.04332, global_step: 30096
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5953 phrases; correct: 5375.
accuracy:  98.53%; precision:  90.29%; recall:  86.81%; FB1:  88.51
LOC: precision:  93.70%; recall:  90.48%; FB1:  92.06  2778
ORG: precision:  86.18%; recall:  84.30%; FB1:  85.23  1302
PER: precision:  88.09%; recall:  83.17%; FB1:  85.56  1873
2019-04-06 11:14:43 epoch 39, step 1, loss: 0.126, global_step: 30097
2019-04-06 11:14:43 epoch 39, step 300, loss: 0.1172, global_step: 30396
2019-04-06 11:14:43 epoch 39, step 600, loss: 0.3963, global_step: 30696
2019-04-06 11:14:43 epoch 39, step 792, loss: 0.08003, global_step: 30888
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 6011 phrases; correct: 5424.
accuracy:  98.57%; precision:  90.23%; recall:  87.60%; FB1:  88.90
LOC: precision:  93.57%; recall:  90.51%; FB1:  92.01  2783
ORG: precision:  85.23%; recall:  84.97%; FB1:  85.10  1327
PER: precision:  88.85%; recall:  85.13%; FB1:  86.95  1901
2019-04-06 11:34:11 epoch 40, step 1, loss: 0.1038, global_step: 30889
2019-04-06 11:34:11 epoch 40, step 300, loss: 0.07421, global_step: 31188
2019-04-06 11:34:11 epoch 40, step 600, loss: 0.1084, global_step: 31488
2019-04-06 11:34:11 epoch 40, step 792, loss: 0.1781, global_step: 31680
===========validation / test===========
processed 177232 tokens with 6192 phrases; found: 5955 phrases; correct: 5382.
accuracy:  98.50%; precision:  90.38%; recall:  86.92%; FB1:  88.61
LOC: precision:  93.94%; recall:  89.92%; FB1:  91.88  2754
ORG: precision:  85.49%; recall:  84.52%; FB1:  85.00  1316
PER: precision:  88.59%; recall:  84.17%; FB1:  86.33  1885
```