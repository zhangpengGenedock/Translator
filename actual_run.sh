python -m nmt.nmt \
    --src=en --tgt=zh \
    --hparams_path=nmt/standard_hparams/wmt16_gnmt_4_layer.json \
    --train_prefix=actual_data/train_seg \
    --dev_prefix=actual_data/dev_seg \
    --test_prefix=actual_data/dev_seg \
    --vocab_prefix=actual_data/vocab \
    --num_gpus=1 \
    --out_dir=model 
   # --num_gpus=2 \
   # --num_train_steps=12000 \
   # --steps_per_stats=100 \
   # --num_layers=2 \
   # --batch_size=16 \
   # --num_units=128 \
   # --dropout=0.2 \
   # --metrics=bleu
