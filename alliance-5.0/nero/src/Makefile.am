## Process this file with automake to produce Makefile.in

#CXXFLAGS        = -g -pg -O2
CXXFLAGS         = -g -O2
#CXXFLAGS        = -O2
AM_CXXFLAGS      = @ALLIANCE_CFLAGS@ \
-I$(top_srcdir)/abl/src \
-I$(top_srcdir)/aut/src \
-I$(top_srcdir)/beh/src \
-I$(top_srcdir)/genlib/src \
-I$(top_srcdir)/mbk/src
AM_CFLAGS        = @ALLIANCE_CFLAGS@ \
-I$(top_srcdir)/abl/src \
-I$(top_srcdir)/aut/src \
-I$(top_srcdir)/beh/src \
-I$(top_srcdir)/genlib/src \
-I$(top_srcdir)/mbk/src 

bin_PROGRAMS     = nero pdv
#noinst_PROGRAMS  = debug

nero_LDADD         = -L$(libdir) @ALLIANCE_LIBS@  \
                   ./libU.a     \
-L$(top_srcdir)/aut/src \
-L$(top_srcdir)/mbk/src \
-L$(top_srcdir)/mbkal/src \
-L$(top_srcdir)/mbkap/src \
-L$(top_srcdir)/mbkedif/src \
-L$(top_srcdir)/mbkhilo/src \
-L$(top_srcdir)/mbkmg/src \
-L$(top_srcdir)/mbkspice/src \
-L$(top_srcdir)/mbkvhdlg/src \
-L$(top_srcdir)/mbkvrlog/src \
-L$(top_srcdir)/mbkvti/src \
                   -lMpu -lMlu  \
                   -lMcl -lMcp  \
                   -lMal -lMap  \
                   -lMsl        \
                   -lMel -lMgl  \
                   -lMhl        \
                   -lMvg        \
                   -lMmg        \
                   -lMlo        \
                   -lMph -lMut  \
                   -lRcn        \
                   -lAut

noinst_LIBRARIES = libU.a


libU_a_SOURCES   = UConst.cpp  \
                   USys.cpp    \
                   UOpts.cpp   \
                   UInter.cpp  \
                   UDefs.h     \
                   MMBK.cpp    \
                   MPower.cpp  \
                   MMBK.h      \
                   MDRGrid.cpp \
                   MNodes.cpp  \
                   MPri.cpp    \
                   MNet.cpp    \
                   MDefs.h     \
                   AAstar.cpp  \
                   ASimple.cpp \
                   ADefs.h     \
                   RBox.cpp    \
                   RMBK.cpp    \
                   RDefs.h

nero_SOURCES     = nero.cpp

pdv_LDADD        = @ALLIANCE_LIBS@  \
-L$(top_srcdir)/aut/src \
-L$(top_srcdir)/mbk/src \
-L$(top_srcdir)/mbkal/src \
-L$(top_srcdir)/mbkap/src \
-L$(top_srcdir)/mbkedif/src \
-L$(top_srcdir)/mbkhilo/src \
-L$(top_srcdir)/mbkmg/src \
-L$(top_srcdir)/mbkspice/src \
-L$(top_srcdir)/mbkvhdlg/src \
-L$(top_srcdir)/mbkvrlog/src \
-L$(top_srcdir)/mbkvti/src \
                   -lMpu -lMlu  \
                   -lMcl -lMcp  \
                   -lMal -lMap  \
                   -lMsl        \
                   -lMel -lMgl  \
                   -lMhl        \
                   -lMvg        \
                   -lMmg        \
                   -lMlo        \
                   -lMph -lMut  \
                   -lRcn        \
                   -lAut

pdv_SOURCES      = pdv.c

#debug_SOURCES    = debug.cpp
