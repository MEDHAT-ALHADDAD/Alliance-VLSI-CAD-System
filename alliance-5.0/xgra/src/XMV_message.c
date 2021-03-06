/*------------------------------------------------------------\
|                                                             |
| This file is part of the Alliance CAD System Copyright      |
| (C) Laboratoire LIP6 - Département ASIM Universite P&M Curie|
|                                                             |
| Home page      : http://www-asim.lip6.fr/alliance/          |
| E-mail support : mailto:alliance-support@asim.lip6.fr       |
|                                                             |
| This progam is  free software; you can redistribute it      |
| and/or modify it under the  terms of the GNU General Public |
| License as  published by the Free Software Foundation;      |
| either version 2 of the License, or (at your option) any    |
| later version.                                              |
|                                                             |
| Alliance VLSI  CAD System  is distributed  in the hope that |
| it  will be useful, but WITHOUT  ANY WARRANTY;              |
| without even the  implied warranty of MERCHANTABILITY or    |
| FITNESS FOR A PARTICULAR PURPOSE. See the GNU General       |
| Public License for more details.                            |
|                                                             |
| You should have received a copy  of the GNU General Public  |
| License along with the GNU C Library; see the file COPYING. |
| If not, write to the Free Software Foundation, Inc.,        |
| 675 Mass Ave, Cambridge, MA 02139, USA.                     |
|                                                             |
\------------------------------------------------------------*/

/*------------------------------------------------------------\
|                                                             |
| Tool    :                   XGRA                            |
|                                                             |
| File    :                  Message.c                        |
|                                                             |
| Authors :              Jacomme Ludovic                      |
|                                                             |
| Date    :                   04.12.96                        |
|                                                             |
\------------------------------------------------------------*/
/*------------------------------------------------------------\
|                                                             |
|                         Include Files                       |
|                                                             |
\------------------------------------------------------------*/

# include <stdio.h>
# include <Xm/Xm.h>
# include <Xm/PushBG.h>
# include <Xm/CascadeBG.h>
 
# include "mut.h"
# include "aut.h"
# include "XSB.h"
# include "XMX.h"
# include "XTB.h"
# include "XMV.h"
# include "XMV_message.h"

/*------------------------------------------------------------\
|                                                             |
|                           Constants                         |
|                                                             |
\------------------------------------------------------------*/
/*------------------------------------------------------------\
|                                                             |
|                            Types                            |
|                                                             |
\------------------------------------------------------------*/
/*------------------------------------------------------------\
|                                                             |
|                          Variables                          |
|                                                             |
\------------------------------------------------------------*/
/*------------------------------------------------------------\
|                                                             |
|                          Functions                          |
|                                                             |
\------------------------------------------------------------*/
/*------------------------------------------------------------\
|                                                             |
|                       XgraPromptZoomIn                     |
|                                                             |
\------------------------------------------------------------*/

void XgraPromptZoomIn()

{
  autbegin();

  XgraDisplayMessage( XGRA_MESSAGE_MODE, "Zoom In" );
  XgraDisplayMessage( XGRA_MESSAGE_INFO, "Select window" );

  switch ( XgraCountEventZoom )
  {
    case 0 : 

      XgraDisplayMessage( XGRA_MESSAGE_PROMPT, "Enter first corner" );

    break;

    case 1 :

      XgraDisplayMessage( XGRA_MESSAGE_PROMPT, "Enter second corner" );
  }

  autend();
}

/*------------------------------------------------------------\
|                                                             |
|                       XgraPromptZoomPan                    |
|                                                             |
\------------------------------------------------------------*/

void XgraPromptZoomPan()

{
  autbegin();

  XgraDisplayMessage( XGRA_MESSAGE_MODE, "Zoom Pan" );
  XgraDisplayMessage( XGRA_MESSAGE_INFO, "Select line"  );

  switch ( XgraCountEventZoom )
  {
    case 0 : 

      XgraDisplayMessage( XGRA_MESSAGE_PROMPT, "Enter source point" );

    break;

    case 1 : 

      XgraDisplayMessage( XGRA_MESSAGE_PROMPT, "Enter target point" );
  }

  autend();
}

/*------------------------------------------------------------\
|                                                             |
|                    XgraPromptZoomCenter                    |
|                                                             |
\------------------------------------------------------------*/

void XgraPromptZoomCenter()

{
  autbegin();

  XgraDisplayMessage( XGRA_MESSAGE_MODE, "Zoom Center" );
  XgraDisplayMessage( XGRA_MESSAGE_INFO, "Select point" );
  XgraDisplayMessage( XGRA_MESSAGE_PROMPT, "Enter center point" );

  autend();
}

