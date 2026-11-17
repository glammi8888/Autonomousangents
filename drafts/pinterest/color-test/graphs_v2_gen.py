# G01–G11 redone in the look Megan picked (LG9 black / LG10 white + photo, pin #100 hand arrows, words in open space), Nov 17.
# Megan: "also can you redo graph 01 02 03 04 05 06 07 08 09 10 11". Old boxed versions kept in ../carousels/graphs-v1/.
# Map: G01 new (manifestation loop) · G02=NG1 · G03=NG2 · G04=NG3 · G05=NG4 · G06=NG5 · G07=NG6 · G08=NG7 · G09=NG8 · G10=LG9 · G11=LG10.
import shutil, graphmix2_gen as m, graphmix_gen  # (re)writes NG*/LG* files
b=m.w(500,300,'desire',m.WH,800,72,'center')+m.sub(500,382,'(clarify)',m.WH,30)+m.w(70,650,'evolve',m.WH,800,72)+m.sub(180,735,'(refine)',m.WH,28)+m.w(70,650,'imagine',m.WH,800,72,'right')+m.sub(820,735,'(rehearse)',m.WH,28)+m.w(500,1150,'act',m.WH,800,72,'center')+m.sub(500,1232,'(participate)',m.WH,30)
b+=m.w(500,860,'continuous<br>creation',m.WH,500,40,'center','font-style:italic')+m.w(50,1310,'the new way of manifestation.',m.WH,800,40,'center',width=900)
m.pin('G01','manifestation loop',True,m.svg(m.ARW,m.WH,14)+b+m.SP(470,560,'#E8A9D4',90))
open('G01.dc.html','w').write(m.P['G01'])
for g,src in zip(['G02','G03','G04','G05','G06','G07','G08','G09','G10','G11'],['NG1','NG2','NG3','NG4','NG5','NG6','NG7','NG8','LG9','LG10']):
    shutil.copy(f'{src}.dc.html',f'{g}.dc.html')
print('ok')
