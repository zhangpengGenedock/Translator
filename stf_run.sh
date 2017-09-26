python -m nmt.nmt \
    --src=en --tgt=zh \
    --hparams_path=nmt/standard_hparams/wmt16.json \
    --train_prefix=stf_data/train_split \
    --dev_prefix=stf_data/dev_split \
    --test_prefix=stf_data/test_seg \
    --vocab_prefix=stf_data/vocab \
    --num_gpus=2 \
    --out_dir=stf_model 
   # --num_gpus=2 \
   # --num_train_steps=12000 \
   # --steps_per_stats=100 \
   # --num_layers=2 \
   # --batch_size=16 \
   # --num_units=128 \
   # --dropout=0.2 \
   # --metrics=bleu
