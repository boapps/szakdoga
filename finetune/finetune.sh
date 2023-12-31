export WANDB_PROJECT="qlora-tasks-7b-v1.9.1"
python qlora.py \
    --model_name_or_path 'huggyllama/llama-7b' \
    --output_dir './qlora-tasks-7b-v1.9.1' \
    --dataset '../datasets/tasks/combined_task_dataset_io_notags' \
    --dataset-format input-output \
    --train_on_source True \
    --learning_rate 0.00006 \
    --num_train_epochs 1 \
    --do_train True \
    --do_eval True \
    --do_mmlu_eval False \
    --bits 4 \
    --source_max_len 2500 \
    --target_max_len 2500 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 4 \
    --logging_first_step true \
    --logging_steps 1 \
    --save_steps 50 \
    --eval_steps 100 \
    --save_strategy steps \
    --save_total_limit 20 \
    --data_seed 42 \
    --warmup_ratio 0.03 \
    --lora_dropout 0.05 \
    --lora_r 16 \
    --bf16 \
    --lora_alpha 8 \
    --weight_decay 0.0 \
    --quant_type nf4 \
    --per_device_eval_batch_size 1 \
    --evaluation_strategy steps \
    --max_memory_MB 12000 \
    --eval_dataset_size 100 \
    --max_eval_samples 100 \
    --lr_scheduler_type constant \
    --report_to "wandb"
