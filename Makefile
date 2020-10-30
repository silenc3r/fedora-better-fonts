clean:
	fd --no-ignore-vcs --type d results --exec rm -rf
	fd --no-ignore-vcs src.rpm --exec rm
	fd --no-ignore-vcs zip --exec rm
	fd --no-ignore-vcs tar.xz --exec rm
	fd --no-ignore-vcs tag.gz --exec rm
	fd --no-ignore-vcs --type f --hidden --regex '^\.build' --exec rm
.PHONY: clean
