"""Vector A3 industrial-design CONCEPT sheets; dimensions are targets, not manufacturing release."""
from pathlib import Path
import math,json
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color

OUT=Path(__file__).resolve().parent
SPEC={'revision':'V4-A','units':'mm','width':160.0,'depth':115.0,'front_height':1.8,'rear_height':6.5,'corner_radius':6.0,'key_band_depth':18.0,'key_count':8,'key_pitch':20.0,'key_travel_target':0.6,'glass_thickness_study':0.7,'clearance_study':0.10,'status':'CONCEPT ONLY - NOT FOR MANUFACTURE','scale_notes':'Orthographic envelope to indicated scale; mechanism and exploded internals are unvalidated arrangement studies.'}
(OUT/'concept-spec.json').write_text(json.dumps(SPEC,indent=2)+'\n')
C=canvas.Canvas(str(OUT/'industrial-design-A3.pdf'),pagesize=(420*mm,297*mm),pageCompression=1)
C.setTitle('Integrated Trackpad V4 | Industrial Design Concept')
C.setAuthor('Trackpad concept study')
INK=HexColor('#252d35');GREY=HexColor('#737e86');LIGHT=HexColor('#cad2d8');BLUE=HexColor('#319eff');MINT=HexColor('#03bba9');GLASS=HexColor('#f8fbfc')

def line(x1,y1,x2,y2,color=INK,w=.22,dash=None):
 C.setStrokeColor(color);C.setLineWidth(w);C.setDash(dash or []);C.line(x1,y1,x2,y2);C.setDash([])
def text(x,y,s,size=2.7,color=INK,align='left'):
 C.setFillColor(color);C.setFont('Helvetica',size)
 getattr(C,{'left':'drawString','center':'drawCentredString','right':'drawRightString'}[align])(x,y,s)
def rect(x,y,w,h,fill=None,stroke=INK,lw=.25,r=0):
 C.setLineWidth(lw);C.setStrokeColor(stroke)
 if fill:C.setFillColor(fill)
 if r:C.roundRect(x,y,w,h,r,stroke=1,fill=int(fill is not None))
 else:C.rect(x,y,w,h,stroke=1,fill=int(fill is not None))
def poly(pts,fill=None,stroke=INK,lw=.25,dash=None):
 C.setLineWidth(lw);C.setStrokeColor(stroke);C.setDash(dash or []);
 if fill:C.setFillColor(fill)
 p=C.beginPath();p.moveTo(*pts[0])
 for pt in pts[1:]:p.lineTo(*pt)
 p.close();C.drawPath(p,stroke=1,fill=int(fill is not None));C.setDash([])
def arrow(x,y,dx,dy,color=INK,l=1.1):
 norm=math.hypot(dx,dy);ux,uy=dx/norm,dy/norm
 poly([(x,y),(x+ux*l-uy*l*.28,y+uy*l+ux*l*.28),(x+ux*l+uy*l*.28,y+uy*l-ux*l*.28)],fill=color,stroke=color,lw=.08)
def dh(x1,x2,y,ref,label):
 for x in [x1,x2]:line(x,ref,x,y+2,GREY,.12)
 line(x1,y,x2,y,GREY,.13);arrow(x1,y,1,0,GREY);arrow(x2,y,-1,0,GREY)
 text((x1+x2)/2,y+1.9,label,2.6,GREY,'center')
def dv(y1,y2,x,ref,label):
 for y in [y1,y2]:line(ref,y,x+2,y,GREY,.12)
 line(x,y1,x,y2,GREY,.13);arrow(x,y1,0,1,GREY);arrow(x,y2,0,-1,GREY)
 C.saveState();C.translate(x-2,y1+(y2-y1)/2);C.rotate(90);text(0,0,label,2.6,GREY,'center');C.restoreState()
def leader(points,label,color=GREY,size=2.5):
 for a,b in zip(points,points[1:]):line(*a,*b,color,.15)
 x,y=points[-1];text(x+2,y-.8,label,size,color)
def badge(x,y,n,color=INK):
 C.setStrokeColor(color);C.setFillColor(HexColor('#ffffff'));C.setLineWidth(.2);C.circle(x,y,3,stroke=1,fill=1);text(x,y-.9,str(n),2.5,color,'center')
def frame(number,title,scale):
 C.saveState();C.scale(mm,mm)
 rect(5,5,410,287,lw=.3)
 text(12,282,'INTEGRATED TRACKPAD / V4',4.0)
 text(12,274,title,3.1,GREY)
 text(408,282,'INDUSTRIAL DESIGN STUDY',2.9,GREY,'right')
 text(408,275,'CONCEPT ONLY - NOT FOR MANUFACTURE',2.6,GREY,'right')
 line(12,269,408,269,LIGHT,.2)
 # Compact conventional drawing title block.
 rect(224,5,191,27,lw=.25)
 for y in [14,23]:line(224,y,415,y,LIGHT,.15)
 for x in [302,344,379]:line(x,5,x,23,LIGHT,.15)
 text(228,26,'FLUSH PIANO-ACTION / WHITE GLASS / ICE BLUE + MINT',2.35)
 text(228,18,'DRAWING: TP-V4-00'+str(number),2.6)
 text(306,18,'REV: A',2.6);text(348,18,'SHEET: '+str(number)+'/3',2.6);text(383,18,'SIZE: A3',2.6)
 text(228,8.5,'SCALE: '+scale,2.55);text(306,8.5,'UNITS: mm',2.55);text(348,8.5,'2026-10-20',2.55);text(383,8.5,'STATUS: STUDY',2.2)
 text(12,23,'ALL DIMENSIONS ARE PROPOSED DESIGN TARGETS.',2.5,GREY)
 text(12,17,'No validated tolerances, material release, BOM or tooling data.',2.4,GREY)
 text(12,11,'Print A3 at 100% for stated scales. Do not scale PNG previews.',2.4,GREY)
def finish():C.restoreState();C.showPage()
def z(y):return 1.8+4.7*y/115

def icon(cx,cy,index):
 if index<4:
  text(cx,cy-1,['SHOT','DRAG','PLAY','VOL'][index],2.0,GREY,'center');return
 dx,dy=[(0,1),(0,-1),(-1,0),(1,0)][index-4];col=BLUE if index<6 else MINT
 line(cx-dx*2.2,cy-dy*2.2,cx+dx*2.2,cy+dy*2.2,col,.45)
 tip=(cx+dx*2.2,cy+dy*2.2)
 for sign in [-1,1]:line(tip[0],tip[1],tip[0]-dx*1.6+dy*1.5*sign,tip[1]-dy*1.6-dx*1.5*sign,col,.45)

# SHEET 1: coherent dimensioned plan / front / side at actual 1:1 envelope.
frame(1,'GENERAL ARRANGEMENT / ORTHOGRAPHIC ENVELOPE','1:1')
x,y=36,124
rect(x,y,160,115,fill=HexColor('#ffffff'),lw=.35,r=6)
line(x,y+97,x+160,y+97,LIGHT,.12)
for i in range(1,8):line(x+20*i,y+97,x+20*i,y+115,LIGHT,.1)
for i in range(8):icon(x+10+20*i,y+106,i)
line(116,119,116,243,LIGHT,.12,[4,1,1,1]);line(31,181.5,201,181.5,LIGHT,.12,[4,1,1,1])
text(116,168,'UNINTERRUPTED WHITE TOUCH SURFACE',2.8,GREY,'center')
text(116,162,'NO DOT MATRIX / NO WRAPAROUND BEZEL',2.4,GREY,'center')
text(x,115,'TOP VIEW',2.8)
dh(36,196,255,239,'160.0')
dh(36,56,245,239,'20.0 PITCH')
dv(124,239,23,36,'115.0')
dv(221,239,209,196,'18.0')
# Section plane through third key.
line(86,118,86,242,GREY,.23,[5,1,1,1]);arrow(86,242,0,-1);arrow(86,118,0,1)
text(89,241,'A',2.8);text(89,116,'A',2.8)
# Front view includes far-rear silhouette; thin actual near edge indicated.
rect(36,72,160,6.5,fill=GLASS,lw=.3);line(36,73.8,196,73.8,GREY,.16)
text(36,85,'FRONT VIEW',2.8);dh(36,196,59,72,'160.0')
leader([(88,73.8),(103,96),(128,96)],'1.8 FRONT LIP TARGET')
# Side profile with front-left and rear-right, same base as front view.
poly([(250,72),(365,72),(365,78.5),(250,73.8)],GLASS,lw=.35)
line(250,72,365,72,GREY,.15)
text(250,85,'RIGHT-SIDE VIEW / FRONT TO REAR',2.8)
dh(250,365,59,72,'115.0');dv(72,78.5,377,365,'6.5')
text(250,67,'FRONT',2.4,GREY);text(365,67,'REAR',2.4,GREY,'right')
leader([(251,73.8),(240,96),(240,104)],'1.8',GREY)
text(250,102,'TAPER: 4.7 / 115 = 2.34 deg',2.6,GREY)
# Design intent notes.
text(248,242,'DESIGN INTENT',3.0)
notes=[('01','One continuous white top plane; low visual mass.'),('02','Eight flush keys within the rear 18 mm band.'),('03','Keys extend to free rear edge; no rear frame.'),('04','Near-invisible seams; clearance is not zero.'),('05','0.6 mm downward travel is a concept target.'),('06','Ice blue: up/down. Mint: left/right.'),('07','Profiles and dimensions define a study envelope.')]
for j,(n,t) in enumerate(notes):text(248,230-j*8,n,2.6,BLUE);text(256,230-j*8,t,2.5)
text(248,161,'Projection: top above front; right-side view to right.',2.35,GREY)
text(248,155,'Visible frame lines show drafting boundaries, not a metal bezel.',2.35,GREY)
finish()

# SHEET 2: full section envelope with enlarged local actuation study.
frame(2,'SECTION A-A / FLUSH KEY ACTUATION CONCEPT','2:1; DETAIL 5:1')
X,Y,S=30,212,2
# Actual proposed side envelope at 2:1.
poly([(X,Y),(X+230,Y),(X+230,Y+13),(X,Y+3.6)],HexColor('#f9fafb'),lw=.35)
# Main glass surface, stop at key band inner edge.
poly([(X,Y+S*z(0)),(X+S*97,Y+S*z(97)),(X+S*97,Y+S*(z(97)-.7)),(X,Y+S*(z(0)-.7))],GLASS,lw=.2)
poly([(X+S*97+.2,Y+S*z(97)),(X+230,Y+13),(X+230,Y+11.6),(X+S*97+.2,Y+S*(z(97)-.7))],HexColor('#e9f7f7'),lw=.25)
text(30,245,'A-A LONGITUDINAL ENVELOPE / 2:1',3.0)
text(30,238,'Front at left; rear / free key edge at right.',2.6,GREY)
dh(30,260,200,212,'115.0')
text(29,207,'FRONT 1.8',2.5,GREY);text(260,207,'REAR 6.5',2.5,GREY,'right')
leader([(241,225),(267,242),(282,242)],'FLUSH REAR KEY',BLUE)
leader([(130,219),(145,230),(165,230)],'MAIN WHITE GLASS',GREY)
text(280,222,'INTERNAL ENVELOPE ONLY',2.65)
text(280,215,'No verified component stack is implied.',2.5,GREY)
text(280,208,'Rear band: 18.0 target',2.5,GREY)
# Local section, real proportions at 5:1, y=90..115.
X,Y,S=30,119,5
px=lambda d:X+(d-90)*S
pz=lambda h:Y+h*S
poly([(px(90),Y),(px(115),Y),(px(115),pz(z(115))),(px(90),pz(z(90)))],HexColor('#fafbfc'),stroke=LIGHT,lw=.2)
# Recessed structural floor.
rect(X,Y,125,2.5,fill=HexColor('#e1e6eb'),stroke=GREY,lw=.2)
# Main fixed glass; a fine draft clearance separates moving key.
poly([(px(90),pz(z(90))),(px(96.9),pz(z(96.9))),(px(96.9),pz(z(96.9)-.7)),(px(90),pz(z(90)-.7))],GLASS,lw=.3)
# Flush rest keytop.
rest=[(px(97),pz(z(97))),(px(115),pz(z(115))),(px(115),pz(z(115)-.7)),(px(97),pz(z(97)-.7))]
poly(rest,HexColor('#edf9fb'),stroke=BLUE,lw=.3)
# Travel overlay: inward key tip goes DOWN; rear remains fixed in this simplified hinge study.
pressed=[(px(97),pz(z(97)-.6)),(px(115),pz(z(115))),(px(115),pz(z(115)-.7)),(px(97),pz(z(97)-1.3))]
poly(pressed,None,stroke=MINT,lw=.35,dash=[2,1])
# Proposed spring/flexure hidden below, schematic only.
line(px(98),pz(1.1),px(108),pz(1.1),GREY,.4)
poly([(px(108),pz(1.1)),(px(111),pz(2.2)),(px(113.5),pz(2.2)),(px(113.5),pz(4.5))],None,GREY,.3)
C.setStrokeColor(GREY);C.setLineWidth(.3);C.circle(px(113.5),pz(4.9),2.0,stroke=1,fill=0)
# Downward actuation vector.
line(px(99),pz(8.8),px(99),pz(z(99)+.5),INK,.3);arrow(px(99),pz(z(99)+.5),0,1)
text(30,174,'KEY DETAIL / 5:1',3.0)
text(30,166,'Blue = rest. Mint dashed = pressed.',2.6,GREY)
leader([(px(97),pz(z(97)-.3)),(53,108),(88,108)],'0.6 TRAVEL TARGET',MINT)
leader([(px(113.5),pz(4.9)),(168,147),(180,147)],'HIDDEN HINGE / FLEXURE STUDY')
leader([(px(115),pz(z(115))),(168,159),(180,159)],'FREE KEY EDGE / NO REAR METAL RAIL')
leader([(px(108),pz(1.1)),(161,125),(180,125)],'RETURN + SENSING TO BE DEVELOPED')
text(30,92,'SURFACE & MECHANISM REQUIREMENTS',2.9)
requirements=['Resting keys align to the same inclined glass plane.','Near-invisible seam: 0.10 study value, not a released tolerance.','0.7 surface thickness is illustrative; material / strength TBD.','Clearance, return force, flexure fatigue, sealing and acoustic feel need prototypes.']
for i,t in enumerate(requirements):text(30,83-i*7,t,2.6,GREY)
# Two profile states, schematic not to scale.
text(294,181,'ACTION STATES / NTS',2.9)
for row,pressed_state in enumerate([False,True]):
 bx,by=295,156-row*37
 line(bx,by,bx+39,by,GREY,.35)
 line(bx+39.8,by-(3 if pressed_state else 0),bx+74,by, MINT if pressed_state else BLUE,.6)
 text(bx,by+9,'PRESS - TIP MOVES DOWN' if pressed_state else 'REST - FLUSH TOP PLANE',2.4)
 if pressed_state:
  line(bx+43,by+12,bx+43,by+1,INK,.25);arrow(bx+43,by+1,0,1)
 text(bx,by-9,'Target stroke 0.6 mm' if pressed_state else 'Fine clearance only',2.4,GREY)
finish()

# SHEET 3: exploded axonometric arrangement; not a released construction model.
frame(3,'EXPLODED ARRANGEMENT / COMPONENT RESPONSIBILITIES','NTS')
AX,AU,AV=.90,-.19,.40
# x = origin + .90*u + .48*v; y = origin - .19*u + .40*v

def point(u,v,ox=40,oy=0):return(ox+.90*u+.48*v,oy-.19*u+.40*v)
def plate(oy,u=0,v=0,w=160,d=115,color=GLASS,stroke=GREY,lw=.25):
 pts=[point(u,v,oy=oy),point(u+w,v,oy=oy),point(u+w,v+d,oy=oy),point(u,v+d,oy=oy)]
 poly(pts,color,stroke,lw);return pts
# Guide lines across the five unassembled layers.
for u,v in [(0,0),(160,0),(160,115),(0,115)]:
 a=point(u,v,oy=70);b=point(u,v,oy=202);line(*a,*b,LIGHT,.12,[2,2])
# 05 recessed shell.
plate(70,color=HexColor('#e8ecef'),stroke=INK,lw=.3)
plate(70,u=5,v=5,w=150,d=105,color=HexColor('#f8f9fa'),stroke=GREY,lw=.15)
# 04 battery and controller placement envelope.
plate(103,color=HexColor('#fafbfc'),stroke=LIGHT,lw=.15)
plate(103,u=28,v=56,w=104,d=35,color=HexColor('#e3e8ec'),stroke=GREY,lw=.2)
plate(103,u=18,v=96,w=124,d=14,color=HexColor('#e8f4f0'),stroke=GREY,lw=.2)
text(*point(80,72,oy=103),'BATTERY ENVELOPE',2.4,GREY,'center')
# 03 eight return / sense positions, hidden mechanisms undecided.
plate(136,u=0,v=97,w=160,d=18,color=HexColor('#edf2f4'),stroke=GREY,lw=.2)
for i in range(8):
 plate(136,u=i*20+3,v=100,w=14,d=10,color=HexColor('#dce9ee'),stroke=GREY,lw=.15)
# 02 sensor/adhesive, limited main pad only.
plate(169,u=0,v=0,w=160,d=97,color=HexColor('#f0f7f8'),stroke=GREY,lw=.2)
for i in range(1,6):
 a=point(0,i*16,oy=169);b=point(160,i*16,oy=169);line(*a,*b,LIGHT,.12)
# 01 main touch face + eight free edge flush keytop pieces at same elevation.
plate(202,u=0,v=0,w=160,d=97,color=HexColor('#ffffff'),stroke=INK,lw=.25)
for i in range(8):
 plate(202,u=i*20+.05,v=97.05,w=19.90,d=17.95,color=HexColor('#ffffff'),stroke=LIGHT,lw=.12)
 p=point(i*20+10,106,oy=202);text(p[0],p[1]-.8,str(i+1),2.5,BLUE if i in [4,5] else MINT if i>5 else GREY,'center')
# Five clear leaders and adjacent descriptions.
items=[(1,202,239,'WHITE TOUCH FACE + FLUSH KEYTOPS','Finish target: satin white; keytop material TBD.'),(2,169,200,'TOUCH SENSOR + BOND LAYER','Concept laminate; active area excludes rear keys.'),(3,136,161,'PER-KEY RETURN / ACTUATION MODULE','Hinge, flexure and sensing are arrangement studies.'),(4,103,122,'POWER / CONTROL PLACEMENT ENVELOPE','No selected battery, electronics or verified BOM.'),(5,70,83,'RECESSED STRUCTURAL BASE','No rim behind key tips; no exposed top metal rail.')]
for n,oy,ly,title,detail in items:
 a=point(160,100,oy=oy);line(*a,265,ly,GREY,.18);line(265,ly,277,ly,GREY,.18);badge(283,ly,n,BLUE if n==1 else GREY)
 text(291,ly+1,title,2.55)
 # one short line per line to keep the technical notes clear.
 words=detail.split();first='';lines=[]
 for word in words:
  if len(first+' '+word)>48:lines.append(first);first=word
  else:first=(first+' '+word).strip()
 if first:lines.append(first)
 for j,t in enumerate(lines):text(291,ly-6-j*4.3,t,2.35,GREY)
text(40,255,'EXPLODED AXONOMETRIC / ARRANGEMENT ONLY',2.8)
text(40,247,'Layer separation exaggerated for clarity; assembled height target remains 1.8 / 6.5 mm.',2.4,GREY)
text(40,43,'No fastener scheme, flexure sizing, glass stress calculation or packaging validation is released.',2.4,GREY)
finish()
C.save()
print(OUT/'industrial-design-A3.pdf')
