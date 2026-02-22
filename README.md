git add .

git commit -m "small change"

git push origin main

Pull on J8 (Termux):
ssh u0_a197@192.168.1.209 -p 8022

cd ~/SitePull/TimeLineBuilder_Server 

git pull

git pull origin main --no-rebase

~./master_server.sh