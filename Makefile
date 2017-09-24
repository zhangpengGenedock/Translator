
run:
	rm -rf model/
	nohup ./actual_run.sh &

board:
	nohup ./tensorboard.sh &
