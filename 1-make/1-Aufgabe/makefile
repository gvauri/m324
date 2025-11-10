ip:
	ipconfig getifaddr en0 > ip

host:
	hostname > host

address:host ip
	echo "$$(cat host)@$$(cat ip)" > address; 

clean:
	rm -f ip host address