a=[[(50,70),(70,90)],[(90,120),(120,150)],[(150,180),(180,210)],[(210,240),(240,270)],[(270,300),(300,340)],[(340,380),(380,420)]]
for b in a:
   print '\\begin{figure}'
   print '\\centering'
   print '\\mbox{'
   print '              \subfigure[]{\epsfig{figure=figures/GBJ1/JetCleaning/Inclusive_selA_Ave_pT_'+str(b[0][0])+'_'+str(b[0][1])+'.eps,width=0.5\\textwidth,height = 6cm}}\quad'
   print '              \subfigure[]{\epsfig{figure=figures/GBJ1/JetCleaning/Inclusive_selA_Ave_pT_'+str(b[1][0])+'_'+str(b[1][1])+'.eps,width=0.5\\textwidth,height = 6cm}}\quad'
   print '                              }'
   print '\\caption[Effect of jet cleaning on the inclusive distribution for $\\bar{p_T}$]{Number of events for each $\Delta y$ bin for Medium and Loose jet cleaning definitions. Shown are (a) $'+str(b[0][0])+'<\\bar{p_T}<'+str(b[0][1])+'$ and (b)$'+str(b[1][0])+'<\\bar{p_T}<'+str(b[1][1])+'$ slices.\label{JetClean'+str(b[0][0])+str(b[0][1])+str(b[1][1])+'}}'
   print '\\end{figure}'
   print ''

