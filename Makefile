
run:
	rm -rf stf_model/
	nohup ./stf_run.sh &

board:
	nohup ./tensorboard.sh &
