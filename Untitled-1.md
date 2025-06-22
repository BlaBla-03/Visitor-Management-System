  <!-- --> <!-- function msoCommentShow(anchor\_id, com\_id) { if(msoBrowserCheck()) { c = document.all(com\_id); a = document.all(anchor\_id); if (null != c && null == c.length && null != a && null == a.length) { var cw = c.offsetWidth; var ch = c.offsetHeight; var aw = a.offsetWidth; var ah = a.offsetHeight; var x = a.offsetLeft; var y = a.offsetTop; var el = a; while (el.tagName != "BODY") { el = el.offsetParent; x = x + el.offsetLeft; y = y + el.offsetTop; } var bw = document.body.clientWidth; var bh = document.body.clientHeight; var bsl = document.body.scrollLeft; var bst = document.body.scrollTop; if (x + cw + ah / 2 > bw + bsl && x + aw - ah / 2 - cw >= bsl ) { c.style.left = x + aw - ah / 2 - cw; } else { c.style.left = x + ah / 2; } if (y + ch + ah / 2 > bh + bst && y + ah / 2 - ch >= bst ) { c.style.top = y + ah / 2 - ch; } else { c.style.top = y + ah / 2; } c.style.visibility = "visible"; } } } function msoCommentHide(com\_id) { if(msoBrowserCheck()) { c = document.all(com\_id); if (null != c && null == c.length) { c.style.visibility = "hidden"; c.style.left = -1000; c.style.top = -1000; } } } function msoBrowserCheck() { ms = navigator.appVersion.indexOf("MSIE"); vers = navigator.appVersion.substring(ms + 5, ms + 6); ie4 = (ms > 0) && (parseInt(vers) >= 4); return ie4; } if (msoBrowserCheck()) { document.styleSheets.dynCom.addRule(".msocomanchor","background: infobackground"); document.styleSheets.dynCom.addRule(".msocomoff","display: none"); document.styleSheets.dynCom.addRule(".msocomtxt","visibility: hidden"); document.styleSheets.dynCom.addRule(".msocomtxt","position: absolute"); document.styleSheets.dynCom.addRule(".msocomtxt","top: -1000"); document.styleSheets.dynCom.addRule(".msocomtxt","left: -1000"); document.styleSheets.dynCom.addRule(".msocomtxt","width: 33%"); document.styleSheets.dynCom.addRule(".msocomtxt","background: infobackground"); document.styleSheets.dynCom.addRule(".msocomtxt","color: infotext"); document.styleSheets.dynCom.addRule(".msocomtxt","border-top: 1pt solid threedlightshadow"); document.styleSheets.dynCom.addRule(".msocomtxt","border-right: 2pt solid threedshadow"); document.styleSheets.dynCom.addRule(".msocomtxt","border-bottom: 2pt solid threedshadow"); document.styleSheets.dynCom.addRule(".msocomtxt","border-left: 1pt solid threedlightshadow"); document.styleSheets.dynCom.addRule(".msocomtxt","padding: 3pt 3pt 3pt 3pt"); document.styleSheets.dynCom.addRule(".msocomtxt","z-index: 100"); } // --> <!-- /\* Font Definitions \*/ @font-face {font-family:Helvetica; panose-1:2 11 6 4 2 2 2 2 2 4;} @font-face {font-family:Courier; panose-1:2 7 4 9 2 2 5 2 4 4;} @font-face {font-family:"Tms Rmn"; panose-1:2 2 6 3 4 5 5 2 3 4;} @font-face {font-family:Helv; panose-1:2 11 6 4 2 2 2 3 2 4;} @font-face {font-family:"New York"; panose-1:2 4 5 3 6 5 6 2 3 4;} @font-face {font-family:System; panose-1:0 0 0 0 0 0 0 0 0 0;} @font-face {font-family:Wingdings; panose-1:5 0 0 0 0 0 0 0 0 0;} @font-face {font-family:"MS Mincho"; panose-1:2 2 6 9 4 2 5 8 3 4;} @font-face {font-family:Batang; panose-1:2 3 6 0 0 1 1 1 1 1;} @font-face {font-family:SimSun; panose-1:2 1 6 0 3 1 1 1 1 1;} @font-face {font-family:PMingLiU; panose-1:2 1 6 1 0 1 1 1 1 1;} @font-face {font-family:"MS Gothic"; panose-1:2 11 6 9 7 2 5 8 2 4;} @font-face {font-family:Dotum; panose-1:2 11 6 0 0 1 1 1 1 1;} @font-face {font-family:SimHei; panose-1:2 1 6 9 6 1 1 1 1 1;} @font-face {font-family:MingLiU; panose-1:2 1 6 9 0 1 1 1 1 1;} @font-face {font-family:Mincho; panose-1:2 2 6 9 4 3 5 8 3 5;} @font-face {font-family:Gulim; panose-1:2 11 6 0 0 1 1 1 1 1;} @font-face {font-family:Century; panose-1:2 4 6 4 5 5 5 2 3 4;} @font-face {font-family:"Angsana New"; panose-1:2 2 6 3 5 4 5 2 3 4;} @font-face {font-family:"Cordia New"; panose-1:2 11 3 4 2 2 2 2 2 4;} @font-face {font-family:Mangal; panose-1:0 0 4 0 0 0 0 0 0 0;} @font-face {font-family:Latha; panose-1:2 0 4 0 0 0 0 0 0 0;} @font-face {font-family:Sylfaen; panose-1:1 10 5 2 5 3 6 3 3 3;} @font-face {font-family:Vrinda; panose-1:0 0 4 0 0 0 0 0 0 0;} @font-face {font-family:Raavi; panose-1:2 0 5 0 0 0 0 0 0 0;} @font-face {font-family:Shruti; panose-1:2 0 5 0 0 0 0 0 0 0;} @font-face {font-family:Sendnya; panose-1:0 0 4 0 0 0 0 0 0 0;} @font-face {font-family:Gautami; panose-1:2 0 5 0 0 0 0 0 0 0;} @font-face {font-family:Tunga; panose-1:0 0 4 0 0 0 0 0 0 0;} @font-face {font-family:"Estrangelo Edessa"; panose-1:0 0 0 0 0 0 0 0 0 0;} @font-face {font-family:"Cambria Math"; panose-1:2 4 5 3 5 4 6 3 2 4;} @font-face {font-family:"Yu Gothic"; panose-1:2 11 4 0 0 0 0 0 0 0;} @font-face {font-family:DengXian; panose-1:2 1 6 0 3 1 1 1 1 1;} @font-face {font-family:Calibri; panose-1:2 15 5 2 2 2 4 3 2 4;} @font-face {font-family:"Calibri Light"; panose-1:2 15 3 2 2 2 4 3 2 4;} @font-face {font-family:"Palatino Linotype"; panose-1:2 4 5 2 5 5 5 3 3 4;} @font-face {font-family:Verdana; panose-1:2 11 6 4 3 5 4 4 2 4;} @font-face {font-family:"Arial Unicode MS"; panose-1:2 11 6 4 2 2 2 2 2 4;} @font-face {font-family:Aptos;} @font-face {font-family:"DengXian Light"; panose-1:2 1 6 0 3 1 1 1 1 1;} @font-face {font-family:"Aptos Display";} @font-face {font-family:"Segoe UI Emoji"; panose-1:2 11 5 2 4 2 4 2 2 3;} @font-face {font-family:Cambria; panose-1:2 4 5 3 5 4 6 3 2 4;} @font-face {font-family:"Segoe UI"; panose-1:2 11 5 2 4 2 4 2 2 3;} @font-face {font-family:"\\@SimSun"; panose-1:2 1 6 0 3 1 1 1 1 1;} /\* Style Definitions \*/ p.MsoNormal, li.MsoNormal, div.MsoNormal {margin:0cm; text-align:justify; line-height:150%; font-size:11.0pt; font-family:"Arial",sans-serif;} h1 {margin-top:20.0pt; margin-right:0cm; margin-bottom:6.0pt; margin-left:21.6pt; text-indent:-21.6pt; line-height:115%; page-break-after:avoid; font-size:20.0pt; font-family:"Arial",sans-serif; font-weight:bold;} h2 {margin-top:18.0pt; margin-right:0cm; margin-bottom:6.0pt; margin-left:28.8pt; text-align:justify; text-indent:-28.8pt; line-height:150%; page-break-after:avoid; font-size:16.0pt; font-family:"Arial",sans-serif; color:black; font-weight:bold;} h3 {margin-top:16.0pt; margin-right:0cm; margin-bottom:4.0pt; margin-left:36.0pt; text-align:justify; text-indent:-36.0pt; line-height:150%; page-break-after:avoid; font-size:14.0pt; font-family:"Arial",sans-serif; color:black; font-weight:bold;} h4 {margin-top:14.0pt; margin-right:0cm; margin-bottom:4.0pt; margin-left:43.2pt; text-align:justify; text-indent:-43.2pt; line-height:150%; page-break-after:avoid; font-size:12.0pt; font-family:"Arial",sans-serif; color:black; font-weight:bold;} h5 {margin-top:12.0pt; margin-right:0cm; margin-bottom:4.0pt; margin-left:50.4pt; text-align:justify; text-indent:-50.4pt; line-height:150%; page-break-after:avoid; font-size:11.0pt; font-family:"Arial",sans-serif; color:#666666; font-weight:normal;} h6 {margin-top:12.0pt; margin-right:0cm; margin-bottom:4.0pt; margin-left:57.6pt; text-align:justify; text-indent:-57.6pt; line-height:150%; page-break-after:avoid; font-size:11.0pt; font-family:"Arial",sans-serif; color:#666666; font-weight:normal; font-style:italic;} p.MsoHeading7, li.MsoHeading7, div.MsoHeading7 {mso-style-link:"Heading 7 Char"; margin-top:2.0pt; margin-right:0cm; margin-bottom:0cm; margin-left:64.8pt; text-align:justify; text-indent:-64.8pt; line-height:150%; page-break-after:avoid; font-size:11.0pt; font-family:"Calibri",sans-serif; color:#243F60; font-style:italic;} p.MsoHeading8, li.MsoHeading8, div.MsoHeading8 {mso-style-link:"Heading 8 Char"; margin-top:2.0pt; margin-right:0cm; margin-bottom:0cm; margin-left:72.0pt; text-align:justify; text-indent:-72.0pt; line-height:150%; page-break-after:avoid; font-size:10.5pt; font-family:"Calibri",sans-serif; color:#272727;} p.MsoHeading9, li.MsoHeading9, div.MsoHeading9 {mso-style-link:"Heading 9 Char"; margin-top:2.0pt; margin-right:0cm; margin-bottom:0cm; margin-left:79.2pt; text-align:justify; text-indent:-79.2pt; line-height:150%; page-break-after:avoid; font-size:10.5pt; font-family:"Calibri",sans-serif; color:#272727; font-style:italic;} p.MsoToc1, li.MsoToc1, div.MsoToc1 {margin-top:0cm; margin-right:0cm; margin-bottom:5.0pt; margin-left:0cm; text-align:justify; line-height:150%; font-size:11.0pt; font-family:"Arial",sans-serif;} p.MsoToc2, li.MsoToc2, div.MsoToc2 {margin-top:0cm; margin-right:0cm; margin-bottom:5.0pt; margin-left:11.0pt; text-align:justify; line-height:150%; font-size:11.0pt; font-family:"Arial",sans-serif;} p.MsoToc3, li.MsoToc3, div.MsoToc3 {margin-top:0cm; margin-right:0cm; margin-bottom:5.0pt; margin-left:22.0pt; text-align:justify; line-height:150%; font-size:11.0pt; font-family:"Arial",sans-serif;} p.MsoToc4, li.MsoToc4, div.MsoToc4 {margin-top:0cm; margin-right:0cm; margin-bottom:5.0pt; margin-left:33.0pt; text-align:justify; line-height:150%; font-size:11.0pt; font-family:"Arial",sans-serif;} p.MsoCommentText, li.MsoCommentText, div.MsoCommentText {mso-style-link:"Comment Text Char"; margin:0cm; text-align:justify; font-size:10.0pt; font-family:"Arial",sans-serif;} p.MsoHeader, li.MsoHeader, div.MsoHeader {mso-style-link:"Header Char"; margin:0cm; text-align:justify; font-size:11.0pt; font-family:"Arial",sans-serif;} p.MsoFooter, li.MsoFooter, div.MsoFooter {mso-style-link:"Footer Char"; margin:0cm; text-align:justify; font-size:11.0pt; font-family:"Arial",sans-serif;} p.MsoCaption, li.MsoCaption, div.MsoCaption {margin-top:0cm; margin-right:0cm; margin-bottom:10.0pt; margin-left:0cm; text-align:justify; font-size:9.0pt; font-family:"Arial",sans-serif; color:#1F497D; font-style:italic;} p.MsoTof, li.MsoTof, div.MsoTof {margin:0cm; text-align:justify; line-height:150%; font-size:11.0pt; font-family:"Arial",sans-serif;} p.MsoTitle, li.MsoTitle, div.MsoTitle {margin-top:0cm; margin-right:0cm; margin-bottom:3.0pt; margin-left:0cm; text-align:justify; line-height:150%; page-break-after:avoid; font-size:26.0pt; font-family:"Arial",sans-serif;} p.MsoSubtitle, li.MsoSubtitle, div.MsoSubtitle {margin-top:0cm; margin-right:0cm; margin-bottom:16.0pt; margin-left:0cm; text-align:justify; line-height:150%; page-break-after:avoid; font-size:15.0pt; font-family:"Arial",sans-serif; color:#666666;} a:link, span.MsoHyperlink {color:blue; text-decoration:underline;} a:visited, span.MsoHyperlinkFollowed {color:purple; text-decoration:underline;} p {margin-right:0cm; margin-left:0cm; font-size:12.0pt; font-family:"Times New Roman",serif;} p.MsoCommentSubject, li.MsoCommentSubject, div.MsoCommentSubject {mso-style-link:"Comment Subject Char"; margin:0cm; text-align:justify; font-size:10.0pt; font-family:"Arial",sans-serif; font-weight:bold;} p.MsoRMPane, li.MsoRMPane, div.MsoRMPane {margin:0cm; font-size:11.0pt; font-family:"Arial",sans-serif;} span.HeaderChar {mso-style-name:"Header Char"; mso-style-link:Header;} span.FooterChar {mso-style-name:"Footer Char"; mso-style-link:Footer;} span.Heading7Char {mso-style-name:"Heading 7 Char"; mso-style-link:"Heading 7"; font-family:"Calibri",sans-serif; color:#243F60; font-style:italic;} span.Heading8Char {mso-style-name:"Heading 8 Char"; mso-style-link:"Heading 8"; font-family:"Calibri",sans-serif; color:#272727;} span.Heading9Char {mso-style-name:"Heading 9 Char"; mso-style-link:"Heading 9"; font-family:"Calibri",sans-serif; color:#272727; font-style:italic;} span.CommentTextChar {mso-style-name:"Comment Text Char"; mso-style-link:"Comment Text";} span.CommentSubjectChar {mso-style-name:"Comment Subject Char"; mso-style-link:"Comment Subject"; font-weight:bold;} span.msoIns {mso-style-name:""; text-decoration:underline; color:teal;} span.msoDel {mso-style-name:""; text-decoration:line-through; color:red;} .MsoChpDefault {font-family:"Arial",sans-serif;} .MsoPapDefault {line-height:115%;} /\* Page Definitions \*/ @page WordSection1 {size:612.0pt 792.0pt; margin:72.0pt 72.0pt 72.0pt 72.0pt;} div.WordSection1 {page:WordSection1;} @page WordSection2 {size:612.0pt 792.0pt; margin:72.0pt 72.0pt 72.0pt 72.0pt;} div.WordSection2 {page:WordSection2;} @page WordSection3 {size:792.0pt 612.0pt; margin:72.0pt 72.0pt 72.0pt 72.0pt;} div.WordSection3 {page:WordSection3;} @page WordSection4 {size:612.0pt 792.0pt; margin:72.0pt 72.0pt 72.0pt 72.0pt;} div.WordSection4 {page:WordSection4;} /\* List Definitions \*/ ol {margin-bottom:0cm;} ul {margin-bottom:0cm;} -->

![](TT6L_G3_SRS_files/image001.gif)

Software Requirements Specification

Campus Wellness Portal with Medical System and Fitness Center Integration

Version: 4.13.0

Date: 05/05/2025

Release By: TT6L - Group 3

Part 1

Part 2

**Student Name**

Student ID

Student Name

Student ID

**Lee Xiang Ze**

1211106818

Ng Jia Hong

1211101788

**Yeoh Han Yi**

1211106319

Lee Ken Yu

1221303813

**Ng Jin Mun**

241UC240BF

Danish Haziq

1221302704

**Yu Ting Hui**

241UC240ZD

**Revisions**

**Version**

**Primary Author(s)**

**Description of Version**

**Date Completed**

4.0

Ng Jia Hong, Lee Ken Yu,

Danish Haziq

This version updates any defects that are found in the previous version from 1.0 � 3.4

15.06.2025

4.1

Ng Jia Hong, Lee Ken Yu,

Danish Haziq

This version updates most of the defects that are found in the from 3.4 � 5.2. Added section 3.8.5 � 3.8.12

22.06.2025

**Table of Content**

[List of Figures� 0](#_Toc201526112)

[List of Table� 2](#_Toc201526113)

[1.0������� Introduction� 3](#_Toc201526114)

[1.1�������� Purpose� 3](#_Toc201526115)

[1.2�������� Scope� 3](#_Toc201526116)

[1.3�������� Product Overview�� 4](#_Toc201526117)

[1.3.1����� Product Perspective� 4](#_Toc201526118)

[1.3.1.1������� System Interfaces� 5](#_Toc201526119)

[1.3.1.2������� User Interfaces� 5](#_Toc201526120)

[1.3.1.3������� Hardware Interfaces� 5](#_Toc201526121)

[1.3.1.4������� Software Interfaces� 5](#_Toc201526122)

[1.3.1.5������� Communications Interfaces� 6](#_Toc201526123)

[1.3.1.6������� Memory Constraints� 6](#_Toc201526124)

[1.3.1.7������� Operations� 6](#_Toc201526125)

[1.3.1.8������� Site Adaptation Requirements� 6](#_Toc201526126)

[1.3.1.9������� Interfaces with Services� 6](#_Toc201526127)

[1.3.2����� Product Functions� 6](#_Toc201526128)

[1.3.3����� User Characteristics� 7](#_Toc201526129)

[1.3.4����� Limitations� 7](#_Toc201526130)

[1.3.4.1������� Regulatory Requirements and Policies� 8](#_Toc201526131)

[1.3.4.2������� Hardware Limitations� 8](#_Toc201526132)

[1.3.4.3������� Interfaces to Other Applications� 8](#_Toc201526133)

[1.3.4.4������� Parallel Operation� 9](#_Toc201526134)

[1.3.4.5������� Audit Functions� 9](#_Toc201526135)

[1.3.4.6������� Control Functions� 9](#_Toc201526136)

[1.3.4.7������� Higher-Order Language Requirements� 9](#_Toc201526137)

[1.3.4.8������� Signal Handshake Protocols� 10](#_Toc201526138)

[1.3.4.9������� Quality Requirements� 10](#_Toc201526139)

[1.3.4.10��������� Criticality of the Application� 10](#_Toc201526140)

[1.3.4.11��������� Safety and Security Considerations� 10](#_Toc201526141)

[1.3.4.12��������� Physical/Mental Considerations� 10](#_Toc201526142)

[1.3.4.13��������� Real-Time Requirements� 11](#_Toc201526143)

[1.4�������� Definitions� 11](#_Toc201526144)

[2.0������� References� 13](#_Toc201526145)

[3.0������� Requirements� 14](#_Toc201526146)

[3.1�������� Product Functions� 14](#_Toc201526147)

[3.1.1����� R1 - Fitness Facility and Class Management 15](#_Toc201526148)

[3.1.2����� R2 - Health Appointment Management 24](#_Toc201526149)

[3.1.3����� R3 - User Access Management 30](#_Toc201526150)

[3.1.4����� R4 - Notification and Alerts� 43](#_Toc201526151)

[3.1.5����� R5 - Personalized Health Content 44](#_Toc201526152)

[3.1.6����� R6 - Wellness Goal and Progress Tracking� 46](#_Toc201526153)

[3.1.7����� R7 - Health and Wellness Report Access� 49](#_Toc201526154)

[3.1.8����� R7 - System Monitoring and Logging� 53](#_Toc201526155)

[3.2�������� Performance Requirements� 54](#_Toc201526156)

[3.3�������� Usability Requirements� 55](#_Toc201526157)

[3.4�������� Interface Requirements� 56](#_Toc201526158)

[3.4.1����� System Interfaces� 56](#_Toc201526159)

[User Interfaces� 57](#_Toc201526160)

[3.4.2����� Hardware Interfaces� 57](#_Toc201526161)

[3.4.3����� Software Interfaces� 57](#_Toc201526162)

[3.4.4����� Communications Interfaces� 58](#_Toc201526163)

[3.5�������� Logical Database Requirements� 58](#_Toc201526164)

[3.6�������� Design Constraints� 60](#_Toc201526165)

[3.7�������� Software System Attributes� 61](#_Toc201526166)

[3.7.1����� Reliability� 61](#_Toc201526167)

[3.7.2����� Availability� 61](#_Toc201526168)

[3.7.3����� Security� 61](#_Toc201526169)

[3.7.4����� Maintainability� 62](#_Toc201526170)

[3.7.5����� Portability� 62](#_Toc201526171)

[3.8�������� Supporting Information� 62](#_Toc201526172)

[3.8.1����� Sample Input/Output Formats & Supporting Artifacts� 63](#_Toc201526173)

[3.8.2����� Supporting or Background Information� 88](#_Toc201526174)

[3.8.3����� Problems to be solved by the Software� 88](#_Toc201526175)

[3.8.4����� Special Packaging Instructions� 89](#_Toc201526176)

[3.8.5����� Validation Session� 0](#_Toc201526177)

[3.8.6����� Defect Summary� 1](#_Toc201526178)

[3.8.7����� Conflict Analysis� 4](#_Toc201526179)

[3.8.8����� Conflict Resolution� 5](#_Toc201526180)

[3.8.9����� Change Log� 6](#_Toc201526181)

[3.8.10������� Requirements Traceability Matrix� 7](#_Toc201526182)

[3.8.11������� Role in Requirements Validation, Negotiation & Management 8](#_Toc201526183)

[3.8.12������� Version Control & Configuration Summary� 8](#_Toc201526184)

[4.0������� Verification� 0](#_Toc201526185)

[4.1�������� Verification Approach� 0](#_Toc201526186)

[4.2�������� Verification Criteria� 1](#_Toc201526187)

[5.0������� Appendices� 3](#_Toc201526188)

[5.1�������� Assumptions and Dependencies� 3](#_Toc201526189)

[5.2�������� Acronyms and Abbreviations� 4](#_Toc201526190)

[5.3�������� Glossary� 4](#_Toc201526191)

List of Figures� 0

List of Table� 2

1.0������� Introduction� 3

1.1�������� Purpose� 3

1.2�������� Scope� 3

1.3�������� Product Overview�� 4

1.3.1����� Product Perspective� 4

1.3.1.1������� System Interfaces� 5

1.3.1.2������� User Interfaces� 5

1.3.1.3������� Hardware Interfaces� 5

1.3.1.4������� Software Interfaces� 5

1.3.1.5������� Communications Interfaces� 6

1.3.1.6������� Memory Constraints� 6

1.3.1.7������� Operations� 6

1.3.1.8������� Site Adaptation Requirements� 6

1.3.1.9������� Interfaces with Services� 6

1.3.2����� Product Functions� 6

1.3.3����� User Characteristics� 7

1.3.4����� Limitations� 7

1.3.4.1������� Regulatory Requirements and Policies� 8

1.3.4.2������� Hardware Limitations� 8

1.3.4.3������� Interfaces to Other Applications� 8

1.3.4.4������� Parallel Operation� 9

1.3.4.5������� Audit Functions� 9

1.3.4.6������� Control Functions� 9

1.3.4.7������� Higher-Order Language Requirements� 9

1.3.4.8������� Signal Handshake Protocols� 10

1.3.4.9������� Quality Requirements� 10

1.3.4.10��������� Criticality of the Application� 10

1.3.4.11��������� Safety and Security Considerations� 10

1.3.4.12��������� Physical/Mental Considerations� 10

1.3.4.13��������� Real-Time Requirements� 11

1.4�������� Definitions� 11

2.0������� References� 13

3.0������� Requirements� 14

3.1�������� Product Functions� 14

3.1.1����� R1 - Fitness Facility and Class Management 15

3.1.2����� R2 - Health Appointment Management 24

3.1.3����� R3 - User Access Management 30

3.1.4����� R4 - Notification and Alerts� 43

3.1.5����� R5 - Personalized Health Content 44

3.1.6����� R6 - Wellness Goal and Progress Tracking� 46

3.1.7����� R7 - Health and Wellness Report Access� 49

3.1.8����� R7 - System Monitoring and Logging� 53

3.2�������� Performance Requirements� 54

3.3�������� Usability Requirements� 55

3.4�������� Interface Requirements� 56

3.4.1����� System Interfaces� 56

User Interfaces� 57

3.4.2����� Hardware Interfaces� 57

3.4.3����� Software Interfaces� 57

3.4.4����� Communications Interfaces� 58

3.5�������� Logical Database Requirements� 58

3.6�������� Design Constraints� 60

3.7�������� Software System Attributes� 61

3.7.1����� Reliability� 61

3.7.2����� Availability� 61

3.7.3����� Security� 61

3.7.4����� Maintainability� 62

3.7.5����� Portability� 62

3.8�������� Supporting Information� 62

3.8.1����� Sample Input/Output Formats & Supporting Artifacts� 63

3.8.2����� Supporting or Background Information� 88

3.8.3����� Problems to be solved by the Software� 88

3.8.4����� Special Packaging Instructions� 89

4.0������� Verification� 89

4.1�������� Verification Approach� 90

4.2�������� Verification Criteria� 91

5.0������� Appendices� 92

5.1�������� Assumptions and Dependencies� 92

5.2�������� Acronyms and Abbreviations� 93

5.3�������� Glossary� 93

**1\. Introduction�������������������������������������������������������������������������������������������������������������� 3**

1.1 Purpose�������������������������������������������������������������������������������������������������������������� 3

1.2 Scope����������������������������������������������������������������������������������������������������������������� 3

1.3 Product Overview����������������������������������������������������������������������������������������������� 4

1.3.1 Product Perspective���������������������������������������������������������������������������������� 4

1.3.1.1 System Interfaces���������������������������������������������������������������������������� 5

1.3.1.2 User Interfaces��������������������������������������������������������������������������������� 6

1.3.1.3 Hardware Interfaces������������������������������������������������������������������������ 6

1.3.1.4 Software Interfaces�������������������������������������������������������������������������� 6

1.3.1.5 Communications Interfaces������������������������������������������������������������� 6

1.3.1.6 Memory Constraints������������������������������������������������������������������������� 6

1.3.1.7 Operations��������������������������������������������������������������������������������������� 6

1.3.1.8 Site Adaptation Requirements��������������������������������������������������������� 6

1.3.1.9 Interfaces with Services������������������������������������������������������������������� 6

1.3.2 Product Functions������������������������������������������������������������������������������������� 7

1.3.3 User Characteristics��������������������������������������������������������������������������������� 7

1.3.4 Limitations������������������������������������������������������������������������������������������������� 8

1.3.4.1 Regulatory Requirements and Policies������������������������������������������� 8

1.3.4.2 Hardware Limitations����������������������������������������������������������������������� 8

1.3.4.3 Interfaces to Other Applications������������������������������������������������������ 8

1.3.4.4 Parallel Operation���������������������������������������������������������������������������� 9

1.3.4.5 Audit Functions�������������������������������������������������������������������������������� 9

1.3.4.6 Control Functions����������������������������������������������������������������������������� 9

1.3.4.7 Higher-Order Language Requirements������������������������������������������� 9

1.3.4.8 Signal Handshake Protocols����������������������������������������������������������� 9

1.3.4.9 Quality Requirements���������������������������������������������������������������������� 9

1.3.4.10 Criticality of the Application��������������������������������������������������������� 10

1.3.4.11 Safety and Security Considerations�������������������������������������������� 10

1.3.4.12 Physical/Mental Considerations�������������������������������������������������� 10

1.3.4.13 Real-Time Requirements������������������������������������������������������������� 10

1.4 Definitions�������������������������������������������������������������������������������������������������������� 10

**2\. References�������������������������������������������������������������������������������������������������������������� 12**

**3\. Requirements��������������������������������������������������������������������������������������������������������� 13**

3.1 Functions���������������������������������������������������������������������������������������������������������� 13

3.2 Performance Requirements����������������������������������������������������������������������������� 44

3.3 Usability Requirements������������������������������������������������������������������������������������ 45

3.4 Interface Requirements����������������������������������������������������������������������������������� 46

3.4.1 System Interfaces����������������������������������������������������������������������������������� 46

3.4.2 User Interfaces���������������������������������������������������������������������������������������� 47

3.4.3 Hardware Interfaces������������������������������������������������������������������������������� 47

3.4.4 Software Interfaces��������������������������������������������������������������������������������� 48

3.4.5 Communications Interfaces�������������������������������������������������������������������� 48

3.5 Logical Database Requirements��������������������������������������������������������������������� 49

3.6 Design Constraints������������������������������������������������������������������������������������������� 51

3.7 Software System Attributes����������������������������������������������������������������������������� 51

3.7.1 Reliability������������������������������������������������������������������������������������������������� 52

3.7.2 Availability����������������������������������������������������������������������������������������������� 52

3.7.3 Security��������������������������������������������������������������������������������������������������� 52

3.7.4 Maintainability����������������������������������������������������������������������������������������� 52

3.7.5 Portability������������������������������������������������������������������������������������������������ 52

3.8 Supporting Information������������������������������������������������������������������������������������ 53

3.8.1 Sample Input/Output Formats & Supporting Artifacts���������������������������� 53

3.8.2 Supporting or Background Information��������������������������������������������������� 67

3.8.3 Problems to be solved by the Software�������������������������������������������������� 68

3.8.4 Special Packaging Instructions��������������������������������������������������������������� 68

**4\. Verification�������������������������������������������������������������������������������������������������������������� 68**

4.1 Verification Approach��������������������������������������������������������������������������������������� 68

4.2 Verification Criteria������������������������������������������������������������������������������������������� 70

**5\. Appendices������������������������������������������������������������������������������������������������������������� 71**

5.1 Assumptions and Dependencies��������������������������������������������������������������������� 71

5.2 Acronyms and Abbreviations��������������������������������������������������������������������������� 72

5.3 Glossary����������������������������������������������������������������������������������������������������������� 72

�

  

List of Figures
===============

[Figure 1.1 Context Diagram.. 4](#_Toc201348251)

[Figure 3.1 Use case diagram.. 14](#_Toc201348252)

[Figure 3.2 Sequence diagram for manage facility. 16](#_Toc201348253)

[Figure 3.3 Sequence diagram for manage fitness class schedule. 19](#_Toc201348254)

[Figure 3.4 Sequence diagram for book facility. 21](#_Toc201348255)

[Figure 3.5 Sequence diagram for book fitness class. 22](#_Toc201348256)

[Figure 3. Sequence diagram for manage appointment 25](#_Toc201348257)

[Figure 3.7 Sequence diagram for cancel / reschedule appointment 27](#_Toc201348258)

[Figure 3.8 Sequence diagram for book health appointment 29](#_Toc201348259)

[Figure 3. Sequence diagram for manage user accounts and roles. 31](#_Toc201348260)

[Figure 3.10 Sequence diagram for log in. 33](#_Toc201348261)

[Figure 3.11 Sequence diagram for receive notification. 43](#_Toc201348262)

[Figure 3.12 Sequence diagram for receive tailored health resources. 44](#_Toc201348263)

[Figure 3.13 Sequence diagram for track wellness progress. 46](#_Toc201348264)

[Figure 3.14 Sequence diagram for set wellness goal 47](#_Toc201348265)

[Figure 3.15 Sequence diagram for view health report 49](#_Toc201348266)

[Figure 3.16� Sequence diagram for view student�s wellness report 50](#_Toc201348267)

[Figure 3.17 Sequence diagram for update student�s wellness report 52](#_Toc201348268)

[Figure 3.18 Sequence diagram for monitor system usage and logs. 53](#_Toc201348269)

[Figure 3.19 Class diagram.. 59](#_Toc201348270)

[Figure 3.20 Microsoft Teams Meeting Attendance Page. 63](#_Toc201348271)

[Figure 3.21 Questionnaire Chart Diagram 1. 64](#_Toc201348272)

[Figure 3.22 Questionnaire Chart Diagram 2. 65](#_Toc201348273)

[Figure 3.23 Questionnaire Chart Diagram 3. 66](#_Toc201348274)

[Figure 3.24 Questionnaire Chart Diagram 4. 66](#_Toc201348275)

[Figure 3.25 Questionnaire Chart diagram 5. 67](#_Toc201348276)

[Figure 3.26 Questionnaire Chart diagram 6. 68](#_Toc201348277)

[Figure 3.27 Questionnaire Chart diagram 7. 68](#_Toc201348278)

[Figure 3.28 Questionnaire Chart diagram 8. 69](#_Toc201348279)

[Figure 3.29 Questionnaire Chart diagram 9. 70](#_Toc201348280)

[Figure 3.30 Questionnaire Chart diagram 10. 70](#_Toc201348281)

[Figure 3.31 Questionnaire Chart diagram 11. 71](#_Toc201348282)

[Figure 3.32 Questionnaire Chart diagram 12. 71](#_Toc201348283)

[Figure 3.33 Questionnaire Chart diagram 13. 72](#_Toc201348284)

[Figure 3.34 Questionnaire Chart diagram 14. 73](#_Toc201348285)

[Figure 3.35 Questionnaire Chart diagram 15. 73](#_Toc201348286)

[Figure 3.36 Questionnaire Chart diagram 16. 74](#_Toc201348287)

[Figure 3.37 Questionnaire Chart diagram 17. 75](#_Toc201348288)

[Figure 3.38 Questionnaire Chart diagram 18. 75](#_Toc201348289)

[Figure 3.39 Questionnaire Chart diagram 19. 76](#_Toc201348290)

[Figure 3.40 Questionnaire Chart diagram 20. 76](#_Toc201348291)

[Figure 3.41 Questionnaire Chart diagram 21. 77](#_Toc201348292)

[Figure 3.42 Questionnaire Chart diagram 22. 78](#_Toc201348293)

[Figure 3.43 Questionnaire Chart diagram 23. 78](#_Toc201348294)

[Figure 3.44 Questionnaire Chart diagram 24. 79](#_Toc201348295)

[Figure 3.45 Questionnaire Chart diagram 25. 79](#_Toc201348296)

[Figure 3.46 Questionnaire Chart diagram 26. 80](#_Toc201348297)

[Figure 3.47 Questionnaire Chart diagram 27. 81](#_Toc201348298)

[Figure 3.48 Questionnaire Chart diagram 28. 81](#_Toc201348299)

[Figure 3.49 Questionnaire Chart diagram 29. 82](#_Toc201348300)

[Figure 3.50 Questionnaire Chart diagram 30. 82](#_Toc201348301)

[Figure 3.51 Questionnaire Chart diagram 31. 83](#_Toc201348302)

[Figure 3.52 Questionnaire Chart diagram 32. 83](#_Toc201348303)

�  

List of Table
=============

[Table 1.1 User Characteristics. 7](#_Toc201348422)

[Table 1.2 Definition. 11](#_Toc201348423)

[Table 3.1 Use case table for manage facility. 15](#_Toc201348424)

[Table 3.2 Use case table for manage fitness class schedule. 17](#_Toc201348425)

[Table 3.3 Use case table for book facility. 20](#_Toc201348426)

[Table 3.4 Use case table for book fitness class. 21](#_Toc201348427)

[Table 3.5 Use case table for manage appointment 23](#_Toc201348428)

[Table 3.6 Use case table for cancel/reschedule appointment 26](#_Toc201348429)

[Table 3.7 Use case table for book health appointment 27](#_Toc201348430)

[Table 3.8 Use case table for manage user accounts and roles. 29](#_Toc201348431)

[Table 3.9 Use case table for log in. 31](#_Toc201348432)

[Table 3.10 Use case table for receive notification. 42](#_Toc201348433)

[Table 3.11 Use case table for receive tailored health resources. 43](#_Toc201348434)

[Table 3.12 Use case table for track wellness progress. 45](#_Toc201348435)

[Table 3.13 Use case table for set wellness goal 46](#_Toc201348436)

[Table 3.14 Use case table for view health report 48](#_Toc201348437)

[Table 3.15 Use case table for view student�s wellness report 49](#_Toc201348438)

[Table 3.16 Use case table for update student�s wellness report 50](#_Toc201348439)

[Table 3.17 Use case table for monitor system usage and logs. 52](#_Toc201348440)

[Table 3.18 Final Requirements Table. 84](#_Toc201348441)

  

1.0     1\. Introduction
========================

1.1   1.1 Purpose
-----------------

The purpose of the �Campus Wellness Portal with Medical System and Fitness Center Integration(Integration (CWPS)� is to empower students to take charge of their holistic well-being by providing a seamless digital platform that facilitates access to medical services, fitness programs and personalized wellness tracking tools.

This document is intended for system developerdevelopers, project manager, configuration manager and client. **�**

1.2   1.2 Scope
---------------

The system is called �Campus Wellness Portal with Medical System and Fitness Center Integration(Integration (CWPS)�. The system will manage the scheduling, tracking and coordination of campus health and fitness services for students. It provides the booking of health center appointments, fitness class registration, personalized wellness goal tracking, user role management and notification support, at the same time, protecting user�s data privacy with encryptions. **�**

In this way, the system will promote overall student wellness by addressing growing concerns over mental and physical health in academic environments. It will provide students with easy access to campus health and fitness services. Therefore, simplifying scheduling for medical appointments and fitness classes. Additionally, the system eases administrative tasks such as system diagnostics and user role management. By offering timely notifications and updates, the system fosters seamless communication between students, doctors and fitness instructors. Additionally, it ensures data privacy and security in compliance with university policies and health data regulations, supporting student well-being through an integrated approach that combines physical health, fitness and emotional support.

  

1.3   1.3 Product Overview
--------------------------

The campus wellness portal is a system that provides an integrated digital platform for students to manage their health condition. With the integration of university�sthe university�s medical system and fitness center the system allows users to:

1.     Direct user to their particular dashboarddashboard based on their role

2.     Book, cancel and reschedule appointments with the campus health center

3.     Register and manage fitness classes and gym sessions

4.     Set and track personalized wellness goals

5.     Access notifications

6.     Redeem prizes by using points earned from achieving wellness goals

7.     Enable staff to manage schedules and view reports

### 1.3.1   1.3.1 Product Perspective

![](TT6L_G3_SRS_files/image002.gif)

_Figure_ 1.1 _Context Diagram_

Figure 1.1 Context Diagram

The Campus Wellness Portal is a subsystem within the University Campus Management System ecosystem which interacts with University Fitness Center and Medical System. It acts as an integrator, providing a user-facing interface while leveraging backend data and functionalities from the integrated system.

#### 1.3.1.1    1.3.1.1 System Interfaces

●       Medical system: Interfaces with university medical system using REST APIs for appointment management and health report.

●       Fitness center system: Interfaces with university fitness center system using REST APIs for class scheduling and facility usage.

#### 1.3.1.2    1.3.1.2 User Interfaces

●       Responsive web-based interface specified for different user roles

●       Accessible to students, health center staff, fitness staff and administrators

●       Must comply with WCAG 2.1 accessibility standards.

�

#### 1.3.1.3    1.3.1.3 Hardware Interfaces

●       Hosted on university-managed servers.

●       Client�s hardware needs to support browsers.

#### 1.3.1.4    1.3.1.4 Software Interfaces

●       Use REST APIs to communicate with external systems (University�s health center system and fitness center system).

●       Use the LDAP system which is implemented by the university for authentication.

●       Data exchange using JSON and XML.

#### 1.3.1.5    1.3.1.5 Communications Interfaces

●       HTTPS-based encrypted communication.

●       Push notifications managedare managed to the university's server via Firebase.

#### 1.3.1.6    1.3.1.6 Memory Constraints

●       Cloud-scalable memory management.

●       Use asynchronous data loading and caching for memory optimization.

●       Use lightweight data storage for goal tracking, class history and user data.

●       Amount of data stored depends on the university's server.

#### 1.3.1.7    1.3.1.7 Operations

●       System operates 24/7 with downtime scheduling.

●       Logs user activities for compliance and monitoring.

●       Includes admin tools for monitoring system usage and managing user accounts.

#### 1.3.1.8    1.3.1.8 Site Adaptation Requirements

●       Admin is allowed to edit user roles therefore each user will have a different dashboard to access different functionalities.

#### 1.3.1.9    1.3.1.9 Interfaces with Services

●       Health and wellness content services for tailored resources.

●       University wide notification services for alerts.

### 1.3.2   1.3.2 Product Functions

●       Login

●       Book health appointment

●       Book fitness class

●       Book facility

●       Receive notification

●       View health report

●       Cancel / Reschedule appointment

●       Receive tailored health resource

●       Track wellness progress

●       Set wellness goal

●       Manage facility

●       Manage fitness class schedule

●       View student�s wellness report

●       Manage appointment

### 1.3.3   1.3.3 User Characteristics

Table 1.1 User Characteristics

_Table_ 1.1 _User_ _Charactheristics_Characteristics

User

Technical Expertise

Usability Considerations

Student

Low

Interface must be visually clear, mobile-responsive and intuitive. The guidanceGuidance onabout how to interact withuse the system should be implemented. Users do notno need to be familiar with the system.

Fitness Center staff

Moderate

Interface should be easy to use, simple and efficient. Users need to be familiar with the system when accessing complicated functions.

Wellness staff

Moderate

Interface should be easy to use, simple and efficient. Users need to be familiar with the system when accessing complicated functions.

System administrator

High

Require full access to user management panels and monitoring dashboards. The users must clearly know what are theythey are doing.

�

### 1.3.4    1.3.4 Limitations

(Mapped to 9.6.7 Limitations)

Describe any limitations that may affect the functionality or performance of the software. Example:

The system is limited to processing research grant applications within specific academic departments.

This section will outline the constraints that may affect the design, development, deployment, functionality and performance of the CWP.

#### 1.3.4.1    1.3.4.1 Regulatory Requirements and Policies

The system will follow university privacy policies and Personal Data Protection Act 2010 (PDPA) to keep the health records and activities logs of the students uncompromised and confidential. Only the authenticated users in the university have access to it. It also has data retention and deletion which is backed up by institutions standards and also allows connection to campus SSO and official SMTP servers.The system must obey university data governance policies, institutional privacy guidelines and applicable health information regulations to ensure that student health records and activity logs are kept secure and confidential. Therefore, the system must comply with Personalthe Personal Data Protection Act 2010 (PDPA) for personal and health data. As a result, this will restrict data access to authenticated university users only. This also helps to enforce data retention and deletion policies according to institutional standards. Besides, the university policy allows integration with the campus SSO and use of official SMTP servers for notifications.

#### 1.3.4.2    1.3.4.2 Hardware Limitations

The system will operate within defined hardware limitations by utilizing university-managed servers which come with performance and storage boundaries. Client access will be limited to standard desktop and mobile browsers with no dependency on specialized input or biometric devices.

#### 1.3.4.3    1.3.4.3 Interfaces to Other Applications

The portal must integrate withintegrate existing external applications including the University Health Center Appointment System, Campus Recreation Center Management Software and Single Sign-On (SSO) authentication services. These integrations will follow specific data formats and protocols. This results in potentially limited API throughput or availability, which will affect third-party providers such as notifications and fitness tracking services. Any changes or downtime in those APIs will directly affect related functionalities such as class booking and appointment scheduling.

#### 1.3.4.4    1.3.4.4 Parallel Operation

The system must operate in parallel with existing systemssystems, including the medical system and fitness center system to enable a phased transition. This parallel operation introduces constraints in data consistency and requires temporary synchronization mechanisms or fallback procedures to prevent service interruptions.

#### 1.3.4.5    1.3.4.5 Audit Functions

The system must record key actions�such as appointment updates, account changes, and role modifications�in timestamped logs. These logs must be securely stored, exportable for audits, and retained for at least 5 years in line with institutional policies.  
The system must provide robust audit functions, recording key activities which include appointment updates, account changes and user role modifications. They are recorded with timestamped logs that can be exported for institutional audits. These logs must be retained securely and comply with audit trail retention policies for 5 years.

#### 1.3.4.6    1.3.4.6 Control Functions

Though the system has limited control over the external systems it depends on, the control over system functions will be enforced using a role-based access control (RBAC) mechanism, ensuring that only authorized personnel can manage sensitive features such as fitness class schedules, appointment slots or user roles isare still needed.

#### 1.3.4.7    1.3.4.7 Higher-Order Language Requirements

The software must be developed programming languages and frameworks which are secure and maintainable. The use of Python for backend services (Flask), JavaScript for frontend services (React) and SQL for data management is aligning with university IT standards. The system will not support legacy languages or platforms.

#### 1.3.4.8    1.3.4.8 Signal Handshake Protocols

The system must fully support HTTP/HTTPS communication standards and handle server responses and errors reliably (HTTP 200, 403, 500). API-level acknowledgements are essential for synchronous booking and cancellation features.

#### 1.3.4.9    1.3.4.9 Quality Requirements

In terms of quality, the system which uses the University�s managed server is expected to achieve at least 99.5% uptime during academic sessions and must be resilient under high-concurrency scenarios, such as during peak appointment booking periods. Automated testing, failover mechanisms and recovery routines are required to ensure reliability.

#### 1.3.4.10                1.3.4.10 Criticality of the Application

The system will handle both real-time health appointments and wellness scheduling. Therefore, it is considered a medium-to-high criticality application as its failure could impact student access to vital health or fitness services.

#### 1.3.4.11                1.3.4.11 Safety and Security Considerations

Strong safety and security measures are required, including data encryption (HTTPS and AES-256), secure session handling and automatic logout after inactivity. Additionally, the system must be protected against cross-site scripting (XSS), SQL injection and session hijacking. Two-factor authentication, 2FA may be mandated for administrative access. This is to ensure data integrity and fluency ofin the operation of the system.

#### 1.3.4.12                1.3.4.12 Physical/Mental Considerations

The system�s interface will consider physical and mental accessibility. It should be usable by students with visual impairments or color blindness and be intuitive for users with limited digital literacy. The system must meet accessibility standards of WCAG 2.1 Level AA compliance and keyboard navigation. For features related to mental health or emotional wellness, the system must use polite and non-triggering language.

#### 1.3.4.13                1.3.4.13 Real-Time Requirements

Since several functions depend on external system APIs, real-time requirements may be impacted by third-party system response times, network latency or downtime. Data may be outdated if the external systems do not push real-time updates or expose polling endpoints. The portal must be able to handle these scenarios gracefully by displaying temporary unavailability messages and queuing updates when necessary.

**�**

1.4    1.4 Definitions
----------------------

Table 1.2 Definition

_Table_ 1.2 _Definition_

**Term**

**Definition**

CWP (Campus Wellness Portal)

The software platform allows students to manage health and fitness services by providing the ability to book appointments, track wellness goals and accessing fitness facilities.

Health Appointment

A scheduled consultation between a student and medical personnel at the university health center.

Fitness Class

A group-based physical activity session offered through the campus fitness center (Zumba, Yoga, etc. )etc.)

Wellness Goal

A personal target set by the student to improve health, such as walking 1 km daily or drinking 2 liters of water.

Wellness Report

A detailed summary of student�sstudents� health and fitness data based on the fitness classes attended and consultancy from the health center.

Booking

The act of reserving a time slot for health appointments, fitness classes and facilities.

Lightweight Directory Access Protocol (LDAP)

A protocol used by the university for user authentication through the single sign-on system.

REST API

A type of web service interface using HTTP methods for communication between systems.

Notification

Alerts that are sent to users via email to inform them about bookings and reminders.

Personal Data Protection Act 2010 (PDPA)

A Malaysian regulation for safeguarding personal data privacy.

Role-Based Access Control (RBAC)

A security mechanism where access to system features is granted based on the user�s role.

Web Content Accessibility Guidelines (WCAG 2.1)

A standard for making web content more accessible to people with disabilities.

Two-Factor Authentication (2FA)

An added security layer requires two forms of verification, such as email TAC, before granting access.

User Acceptance Testing (UAT)

A testing phase where end users verify the system meets their needs and requirements.

Docker

A platform used to package software into containers for consistent deployment across environments.

2.0     2\. References
======================

_Web Content Accessibility Guidelines (WCAG) 2.1. (2025, May 6). [https://www.w3.org/TR/WCAG21/](https://www.w3.org/TR/WCAG21/)_

Ppdp, P. (2024, September 20). PDP Act 2010 � Personal Data Protection. Perlindungan Data Peribadi (PDP). https://www.pdp.gov.my/ppdpv1/en/akta/pdp-act-2010/

_What is a REST API?_ (n.d.). [https://www.redhat.com/en/topics/api/what-is-a-rest-api](https://www.redhat.com/en/topics/api/what-is-a-rest-api)

"ISO/IEC/IEEE International Standard - Systems and software engineering -- Life cycle processes -- Requirements engineering," in ISO/IEC/IEEE 29148:2018(E) , vol., no., pp.1-104, 30 Nov. 2018, doi: 10.1109/IEEESTD.2018.8559686. https://doi.org/10.1109/IEEESTD.2018.8559686

Holicki, R. (2021, April 8). _How can you interpret your Kano results?_ SEEBURGER Blog. [](https://blog.seeburger.com/how-can-you-interpret-your-kano-results/)[https://blog.seeburger.com/how-can-you-interpret-your-kano-results/](https://blog.seeburger.com/how-can-you-interpret-your-kano-results/)

Ashtari, H. (2023, February 6). _Simple Mail Transfer Protocol (SMTP)._ Spiceworks. [](https://www.spiceworks.com/tech/networking/articles/simple-mail-transfer-protocol-smtp/)[https://www.spiceworks.com/tech/networking/articles/simple-mail-transfer-protocol-smtp/](https://www.spiceworks.com/tech/networking/articles/simple-mail-transfer-protocol-smtp/)

**�**

  

 

3.0   3\. Requirements
======================

3.1    3.1 Product Functions
----------------------------

![](TT6L_G3_SRS_files/image003.gif)

Figure 3.1 Use case diagram  

Table 3.1 Use case table for manage facility

### 3.1.1   R1 - Fitness Facility and Class Management

_Table_ 3.1 _Use case table for manage facility_

Section

UC-013.1.1

Name

Manage facility

Author

Yeoh Han Yi

Source

Fitness Center Staff (Stakeholder)

Short description

Fitness Center Staff can manage campus fitness facilities, which include updating facility status and adding new facilities.

Goal

To ensure that the information about the available facilities are always accurate and updated in the system.

Actor

Fitness Center Staff

Pre-condition

User is logged in as Fitness Center Staff

Post-condition

1.  Facility data is updated
2.  A new facility is successfully added into the system.

Main flow

1.  Fitness center staff click into the manage facility page.
2.  The system retrieves the facilities data from the database.
3.  The system displays the list of facilities including status to the fitness center staff.
4.  Fitness center staff selects a facility to update.
5.  The system requires fitness center staff to input the new facility details.
6.  Fitness center staff enter the new information and click the submit button.
7.  System will validate the validity of the information input and store the updated information into the database.
8.  System prompts a successful update message to the fitness center staff.

Alternative flow

●       Update validation fail

1.     Fitness center staff entered the invalid input such as invalid character or empty name.

2.     System prompts an error message and requests fitness center staff to enter a valid input.

3.     Back to main flow step 5.

Relationship to other use cases

Related to �Book facility� use case

![](TT6L_G3_SRS_files/image004.jpg)

  
[\[D1\]](#_msocom_1) 

_Figure_ 3.2 _Sequence diagram for manage facility_

Figure 3.2 Sequence diagram for manage facility

Table 3.2 Use case table for manage fitness class schedule

_Table_ 3.2 _Use case table for manage fitness class schedule_

Section

UC-023.1.2

Name

Manage fitness class schedule

Author

Yeoh Han Yi

Source

Fitness Center Staff (Stakeholder)

Short description

Fitness Center Staff can manage the schedule of the fitness classes for students to view and book.

Goal

To provide a flexible and accurate schedule for fitness classes so that students could view and book effectively.

Actor

Fitness Center Staff

Pre-condition

User is logged in as Fitness Center Staff

Post-condition

1.  Class schedule is added

��������������� or

2.  Class schedule is edited

��������������� or

3.  Class schedule is deleted

Main flow

1.  Fitness center staff clicks into manage fitness class schedule page.
2.  The system retrieves the fitness class data from the database.
3.  The system displays the existing fitness classes to fitness center staff.
4.  Fitness center staff can choose to add a new class, edit a class, or delete a class.
5.  If the fitness center staff choose to add a new class, the system requests fitness center staff to enter the required information such as class name, instructor, time etc.
6.  If the fitness center staff choose to edit a class schedule, fitness center staff select an existing class. The system displayed the class schedule details and the fitness center staff could modify the details.
7.  If the fitness center staff choose to delete a class, fitness center staff select an existing class and click on the delete icon. The system prompts a confirmation message to make sure that this class schedule is going to be deleted from the database.
8.  Fitness center staff click the submit button.
9.  The system will validate the inputs from fitness center staff.
10.  System update the database.
11.  System prompts a success message to fitness center staff.

Alternative flow

●       New class time conflict

1.     Fitness center staff adds a new class schedule in a classroom that is already booked at that particular time.

2.     System displays a warning message to fitness center staff.

3.     Back to main flow step 4.

●       Input validation fail

1.     Fitness center staff entered the invalid input such as invalid character or empty name.

2.     System prompts an error message and requests fitness center staff to enter a valid input.

3.     System requires fitness center staff to input the required information again.

4.     Back to main flow 8.

Relationship to other use cases

Related to �Book fitness class� use case

![](TT6L_G3_SRS_files/image005.jpg)  

_Figure_ 3.3 _Sequence diagram for manage fitness class schedule_

Figure 3.3 Sequence diagram for manage fitness class schedule

Table 3.33.6 Use case table for book facility

Section

UC-03

Name

Book facility

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Student books facilities like gym rooms or sports courts based on date and time they have chosen

Goal

Allow student to reserve a facility slot based on availability

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Facility booking is recorded in the database

Main Flow

1.  Student selects the type of facility to book.
2.  Student selects the date and time for using the facility.
3.  System fetches the available facilities from the database.
4.  Database returns the available facilities to the system.
5.  If there�s at least one available facility, system displays the available facilities.
6.  Student selects the facility.
7.  System records the facility booking.

Alternative Flow

No available facility

1.  System displays an error message.
2.  2\. Student clicks �Join Waitlist�.
3.  3\. System records the student to the waitlist.
4.  4\. System detects when a slot becomes available.
5.  5\. System notifies the student.

Relationship to other use cases

Related to �Manage facility� use case

![](TT6L_G3_SRS_files/image006.jpg)  

Figure 3.43.53.7 Sequence diagram for book facility

Table 3.43.8 Use case table for book fitness class

Section

UC-04

Name

Book fitness class

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Enables student to book available fitness classes such as yoga, HIIT, or Zumba

Goal

Student registers for a fitness class in advance

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Student is enrolled in the selected class

Main Flow

1.  Student selects the date and time.
2.  System fetches the available slots from the database.
3.  Database returns the available slots to the system.
4.  If there�s at least one available slot, the system displays the available slots.
5.  Student selects their desired slot.
6.  System saves the booking record.

Alternative Flow

No available slot

1.  System displays an error message.

2.     2\. Student clicks �Join Waitlist�.

3.     3\. System records the student to the waitlist.

4.     4\. System detects when a slot becomes available.

5.     5\. System notifies the student.

Relationship to other use cases

Related to �Manage fitness class schedule� use case

![](TT6L_G3_SRS_files/image007.gif)  

Figure 3.3.9 Sequence diagram for book fitness class

Table 3.3 Use case table for manage appointment

### 3.1.2   R2 - Health Appointment Management

Table 3.�Use case table for manage appointment

Section

UC-053.1.3

Name

Manage Appointment

Author

Yeoh Han Yi

Source

Wellness Staff (Stakeholder)

Short description

Wellness staff can manage the appointment schedule by creating, editing or deleting the slots based on the doctor�s availability.

Goal

To allow wellness staff to manage appointment slots efficiently so that students can book health consultations.

Actor

Wellness Staff

Pre-condition

User is logged in as Wellness Staff

Post-condition

Appointment slots are successfully created, updated or removed from the system.

Main flow

1.  Wellness staff click into the manage appointment page.
2.  The system retrieves the appointment data from the database.
3.  The system displays the existing appointment to wellness staff.
4.  Wellness staff can choose to create slots, edit slots or remove slots for students to make appointments.
5.  If the wellness staff choose to add new slots, the system requests wellness staff to enter the required information such as date time and location.
6.  If the wellness staff choose to edit slots, wellness staff select an existing slot. The system displayed the slot details and the wellness staff could modify the details.
7.  If the wellness staff choose to remove slots, wellness staff select an existing slot and click on the delete icon. The system prompts a confirmation message to make sure that this slot is going to be deleted from the database.
8.  Wellness staff click the submit button.
9.  The system will validate the inputs from wellness staff.
10.  System update the database.
11.  System prompts a success message to wellness staff.

Alternative flow

●       Input validation fail

1.     Wellness staff entered the invalid input such as invalid character or empty name.

2.     System prompts an error message and requests wellness staff to enter a valid input.

3.     Back to main flow step 8.

●       Time slot unavailable

1.     Wellness staff selects a time that is already booked for the same doctor.

2.     System prompts a warning message to the wellness staff.

3.     Back to main flow 4.

Relationship to other use cases

Related to �Book health appointment� use case.

![Figure 3.7 Sequence diagram for manage appointment](TT6L_G3_SRS_files/image008.gif)

  
[\[D2\]](#_msocom_2) 

Figure 3.4 Sequence diagram for manage appointment

Table 3.63.9 Use case table for cancel/reschedule appointment

Section

UC-06

Name

Cancel / Reschedule appointment

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Student cancels or modifies the booking of a fitness class

Goal

Enable student to update or remove their fitness class reservations

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Booking is either canceled or updated

Main Flow

1.  Student goes to the appointment list page.
2.  System fetches the appointments from the database.
3.  Database returns the appointment list.
4.  System displays the appointment list.
5.  Student selects one of the appointments.
6.  If the student wants to cancel appointment

1.  Student presses the �cancel� button.
2.  System deletes the appointment from the database.

8.  If the student wants to reschedule appointment

1.  Student selects the new date and time.
2.  System updates the new date and time of appointment.

10.  System displays the updated appointment list.

Relationship to other use cases

Related to �Book health appointment� use case

![A blue and white diagram
AI-generated content may be incorrect.](TT6L_G3_SRS_files/image009.gif)  

Figure 3.3.10 Sequence diagram for cancel / reschedule appointment

Table 3.73.�Use case table for book health appointment

Section

UC-07

Name

Book health appointment

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Students schedules a medical appointment with the university health center

Goal

Enable student to select a date, time, and doctor for a health appointment

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Appointment details are stored in the database only after the system confirms no conflicting appointment exists for the selected time slot.[\[N3\]](#_msocom_3) 

Main Flow

1.  Student selects the date and time.
2.  System fetches the available slots from the database.
3.  Database returns the available slots to the system.
4.  If there�s at least one available slot, the system displays the available slots.
5.  Student selects their desired slot.
6.  System performs a double-booking check to ensure the selected slot is not already taken.[\[N4\]](#_msocom_4) 
7.  System saves the appointment record.

Alternative Flow

No available slot

1.  System displays an error message.
2.  2\. Student clicks �Join Waitlist�.
3.  3\. System records the student to the waitlist.
4.  4\. System detects when a slot becomes available.
5.  5\. System notifies the student.

Relationship to other use cases

Related to �Manage appointment� use case

![](TT6L_G3_SRS_files/image010.gif)

  

Figure 3.3.8 Sequence diagram for book health appointment

### 3.1.3   R3 - User Access Management

Table 3.4 Use case table for manage user accounts and roles

Table 3.8 Use case table for manage user accounts and roles

Section

UC-083.1.4

Name

Manage User Accounts and Roles

Author

Yeoh Han Yi

Source

System Administrator (Stakeholder)

Short description

System administrators can manage users by creating, editing and deleting the user accounts. Also, system administrators are able to update the user roles.

Goal

To allow the system administrator to maintain user records and roles.

Actor

System Administrator

Pre-condition

User is logged in as system administrator

Post-condition

User records are displayed, updated, deleted or modified as per administrator actions.

Main flow

1.  System administrator clicks into the manage user accounts and roles page.
2.  The system retrieves the usersuser�s data from the database.
3.  The system displays the user's data to the system administrator.
4.  System administratoradministrators can choose to create new userusers, edit user accountaccounts, delete user accountaccounts and update user roleroles.
5.  If the system administrator chooses to create a new user, the system requests the system administrator to enter the required information such as username and password.
6.  If the system administrator chooses to edit the user account, the system administrator selects an existing account. The system displays the user informationinformation, and the system administrator could modify the details.
7.  If the system administrator chooses to delete the user account, the system administrator selects an existing account and clicks on the delete icon. The system prompts a confirmation message to make sure that this user account is going to be deleted from the database.
8.  System administrator clicks the submit button.
9.  The system will validate the inputs from the system administrator.
10.  System updateupdates the database.
11.  System prompts a success message to the system administrator.

Alternative flow

●       Input validation failfails

1.     System administrator entered the invalid input such as invalid character or empty name.

2.     System prompts an error message and requests system administrator to enter a valid input.

3.     Back to main flow step 8.

●       Username already existexists

1.     System administratoradministrators try to create a user with an existing username.

2.     System prompts a warning message to system administrator.

3.     Back to main flow step 5.

Relationship to other use cases

Related to �User Login� use case.

![](TT6L_G3_SRS_files/image011.jpg)

Figure 3.�Sequence diagram for manage user accounts and roles

Figure 3.5 Sequence diagram for manage user accounts and roles

Table 3.5� Use case table for log in

Table 3.�Use case table for log in

Section

UC-093.1.5

Name

Log in

Author

Ng Jin Mun

Source

Student (Stakeholder), System Administrator (Stakeholder),� Fitness), Fitness Center Staff (Stakeholder), Wellness Staff (Stakeholder)

Short Description

User logs in securely to access personalized features of the portal

Goal

To verify user identity before granting access to the system

Actor

Student, System Administrator,� FitnessAdministrator, Fitness Center Staff, Wellness Staff

Pre-condition

User has a registered account

Post-condition

User is successfully logged in and redirected to the dashboard.

OR

If login fails, an error message is shown.

Main Flow

1.  User enters credentials.
2.  System verifies the user's credentials with the LDAPdatabase.
3.  Database LDAP checks if the user exists and returns the result.
4.  If the user exists, the system grants access and redirects the user to the dashboard.

Alternative Flow

User does not exist

1.  System displays an error message indicating authentication failure.

Relationship to other use cases

\-Related to �Manage User Accounts and Roles� where user credentials and roles are maintained.

![](TT6L_G3_SRS_files/image012.gif)  
[\[D5\]](#_msocom_5) 

![Figure 3. Sequence diagram for log in](TT6L_G3_SRS_files/image013.gif)

  

Figure 3.6 Sequence diagram for log in

Table 3.6� Use case table for book facility

Table 3.6 Use case table for book facility

Section

3.1.6

Name

Book facility

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Student books facilities like gym rooms or sports courts based on date and time they have chosen

Goal

Allow student to reserve a facility slot based on availability

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Facility booking is recorded in the database

Main Flow

1.  Student selects the type of facility to book.
2.  Student selects the date and time for using the facility.
3.  System fetches the available facilities from the database.
4.  Database returns the available facilities to the system.
5.  If there�s at least one available facility, system displays the available facilities.
6.  Student selects the facility.
7.  System records the facility booking.

Alternative Flow

No available facility

1.  System displays an error message.

Relationship to other use cases

Related to �Manage facility� use case

![](TT6L_G3_SRS_files/image014.gif)

Figure 3.7 Sequence diagram for book facility

Figure 3.7 Sequence diagram for book facility

Table 3.7� Use case table for book health appointment

Table 3.7 Use case table for book health appointment

Section

3.1.7

Name

Book health appointment

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Students schedules a medical appointment with the university health center

Goal

Enable student to select a date, time, and doctor for a health appointment

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Appointment details are stored in the database

Main Flow

1.  Student selects the date and time.
2.  System fetches the available slots from the database.
3.  Database returns the available slots to the system.
4.  If there�s at least one available slot, the system displays the available slots.
5.  Student selects their desired slot.
6.  System saves the appointment record.

Alternative Flow

No available slot

1.  System displays an error message.

Relationship to other use cases

Related to �Manage appointment� use case

![](TT6L_G3_SRS_files/image015.gif)

Figure 3.8 Sequence diagram for book health appointment

Figure 3.8 Sequence diagram for book health appointment

Table 3.8� Use case table for book fitness class

Table 3.8 Use case table for book fitness class

Section

3.1.8

Name

Book fitness class

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Enables student to book available fitness classes such as yoga, HIIT, or Zumba

Goal

Student registers for a fitness class in advance

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Student is enrolled in the selected class

Main Flow

1.  Student selects the date and time.
2.  System fetches the available slots from the database.
3.  Database returns the available slots to the system.
4.  If there�s at least one available slot, the system displays the available slots.
5.  Student selects their desired slot.
6.  System saves the booking record.

Alternative Flow

No available slot

1.  System displays an error message.

Relationship to other use cases

Related to �Manage fitness class schedule� use case

![](TT6L_G3_SRS_files/image016.gif)

Figure 3.9 Sequence diagram for book fitness class

Figure 3.9 Sequence diagram for book fitness class

Table 3.9� Use case table for cancel/reschedule appointment

Table 3.9 Use case table for cancel/reschedule appointment

Section

3.1.9

Name

Cancel / Reschedule appointment

Author

Ng Jin Mun

Source

Student (Stakeholder)

Short Description

Student cancels or modifies the booking of a fitness class

Goal

Enable student to update or remove their fitness class reservations

Actor

Student

Pre-condition

Student logins to the system

Post-condition

Booking is either canceled or updated

Main Flow

1.  Student goes to the appointment list page.
2.  System fetches the appointments from the database.
3.  Database returns the appointment list.
4.  System displays the appointment list.
5.  Student selects one of the appointments.
6.  If the student wants to cancel appointment

1.  Student presses the �cancel� button.
2.  System deletes the appointment from the database.

8.  If the student wants to reschedule appointment

1.  Student selects the new date and time.
2.  System updates the new date and time of appointment.

10.  System displays the updated appointment list.

Relationship to other use cases

Related to �Book health appointment� use case

![](TT6L_G3_SRS_files/image017.gif)

Figure 3.10 Sequence diagram for cancel / reschedule appointment

Figure 3.10 Sequence diagram for cancel / reschedule appointment

### 3.1.4   R4 - Notification and Alerts

Table 3.10 Use case table for receive notification

Table 3.10 Use case table for receive notification

Section

UC-103.1.10

Name

Receive Notification

Author

Yu Ting Hui

Source

Student (Stakeholder)

Short Description

The system will send a booking reminder to user

Goal

To keep student informed about their health appointment and fitness class

Actor

Student

Pre-condition

1.  Student has enabled notifications
2.  Student has make booking on the health appointment, fitness class or the facilities

Post-condition

Student receives and views the notification

Main Flow

1.  The student accesses the notification section in the system interface.
2.  The system checks for new notifications assigned to the user.
3.  The system queries the database for all notifications linked to the user based on user ID.
4.  The database returns any matching notification records.
5.  The system displays the notification to the user in the notification dashboard.

Relationship to other use cases

Related to �Book health appointment�, �Book Fitness Class� and �Book Facilities� use case

![](TT6L_G3_SRS_files/image018.gif)

Figure 3.12 Sequence diagram for receive notification

Figure 3.11 Sequence diagram for receive notification  
  

### 3.1.5   R5 - Personalized Health Content

Table 3.11 Use case table for receive tailored health resources

Table 3.11 Use case table for receive tailored health resources

Section

UC-113.1.11

Name

Receive Tailored Health Resources

Author

Yu Ting Hui

Source

Student (Stakeholder)

Short Description

The system provides health education or support resources that customized to student�s health profile

Goal

To deliver relevant and personalized health information to support wellness

Actor

Student

Pre-condition

User has submitted health data or preferences

Post-condition

User receives and can access relevant health resources

Main Flow

1.  The student accesses the tailored health resources section in the system interface.
2.  The system retrieves the user's profile data (e.g., age, gender, health goals, or preferences).
3.  The system queries the database for health resources that match the user�s profile or preferences.
4.  The database returns a list of matching health resources (e.g., articles, videos, diet tips).
5.  The system displays the tailored health resources on the user interface.

Relationship to other use cases

\-

![](TT6L_G3_SRS_files/image019.gif)  

Figure 3.�Sequence diagram for receive tailored health resources

Figure 3.12 Sequence diagram for receive tailored health resources

### 3.1.6   R6 - Wellness Goal and Progress Tracking

Table 3.12 Use case table for track wellness progress

Table 3.12 Use case table for track wellness progress

Section

UC-123.1.12

Name

Track Wellness Progress

Author

Yu Ting Hui

Source

Student (Stakeholder)

Short Description

Student able to track and monitor their health activities and progress

Goal

To monitor improvements or setbacks in wellness based on set goals or daily habit

Actor

Student

Pre-condition

User has wellness data to input

Post-condition

System records, displays, and updates wellness progress

Main Flow

1.  The student accesses the wellness progress section in the system interface.
2.  The system retrieves wellness data for the user (e.g., activity logs, goals achieved, step counts, sleep hours).
3.  The system calculates progress based on current data vs. set goals (if any).
4.  The system generates visual indicators (e.g., graphs, progress bars, charts).
5.  The system displays the wellness progress to the user.

Relationship to other use cases

\-Related to **Set Wellness Goal (3.1.13)**, as goals influence what is tracked

  
![](TT6L_G3_SRS_files/image020.gif)  

Figure 3.�Sequence diagram for track wellness progress

Figure 3.13 Sequence diagram for track wellness progress

Table 3.13 Use case table for set wellness goal

Table 3.13 Use case table for set wellness goal

Section

UC-133.1.13

Name

Set Wellness Goal

Author

Yu Ting Hui

Source

Student (Stakeholder)

Short Description

Student able to set personal wellness targets

Goal

To enable the customization of health goals based on individual needs and lifestyle

Actor

Student

Pre-condition

Student is authenticated and able to interact with system

Post-condition

Wellness goal is saved and used for tracking

Main Flow

1.  The student accesses the set wellness goal section in the system interface.
2.  The student inputs the desired wellness goal. (e.g., exercise 30 minutes/day, sleep 7 hours/day, increase fiber intake to 25�30g per day).
3.  The system receives the input and validates it.
4.  If the input is valid:

1.  The system stores the wellness goal in the database.
2.  The system displays a success message: �Goal set successfully.�

6.  If the input is invalid:

1.  The system displays an error message: �Please insert again.�

Relationship to other use cases

Related to �Track Wellness Progress� use case

![](TT6L_G3_SRS_files/image021.gif)  

Figure 3.�Sequence diagram for set wellness goal

Figure 3.14 Sequence diagram for set wellness goal

### 3.1.7   R7 - Health and Wellness Report Access

Table 3.14 Use case table for view health report

Table 3.14 Use case table for view health report

Section

UC-143.1.14

Name

View Health Report

Author

Lee Xiang Ze

Source

Student (Stakeholder)

Short Description

Student is able to view health data recorded.

Goal

Allow student to monitor health status and take required actions.

Actor

Student

Pre-condition

1.  Student is authenticated and able to interact with the system.
2.  Student must at least go to the wellness center and fitness center once.

Post-condition

Health status is shown based on data recorded.�

Main Flow

1.  Student clicks on view report.
2.  System displays details of the health report of the student.

Relationship to other use cases

![](TT6L_G3_SRS_files/image022.gif)  

Figure 3.�Sequence diagram for view health report

Figure 3.14e Sequence diagram for view health report

Table 3.15 Use case table for view student�s wellness report

Table 3.15 Use case table for view student�s wellness report

Section

UC-153.1.15

Name

View Student�s Wellness Report

Author

Lee Xiang Ze

Source

Fitness Center Staff (Stakeholder), Wellness Staff (Stakeholder)

Short Description

Staff is able to view student�s health data recorded.

Goal

Allow staff to know health status and take required actions.

Actor

Fitness Center Staff, Wellness Staff

Pre-condition

1.  Staff is authenticated and able to interact with system.
2.  Staff must know targeted student�s id.

Post-condition

Health detail is shown based on data recorded.�

Main Flow

1.  Staff clicks on view wellness report.
2.  System displays a list of students� reports.
3.  Staff clicks on desired report.
4.  System displays full details of the student�s report.

Relationship to other use cases

Will show report using view student�s wellness report when user wants to update student�s wellness report

![](TT6L_G3_SRS_files/image023.gif)  

Figure 3.��Sequence diagram for view student�s wellness report

Figure 3.15 Sequence diagram for view student�s wellness report

Table 3.16 Use case table for update student�s wellness report

Table 3.16 Use case table for update student�s wellness report

Section

UC-163.1.16

Name

Update Student�s Wellness Report

Author

Lee Xiang Ze

Source

Fitness Center Staff (Stakeholder), Wellness Staff (Stakeholder)

Short Description

Staff is able to update student�s health data recorded.

Goal

Allow staff to update student�s health status based on observation.

Actor

Fitness Center Staff, Wellness Staff

Pre-condition

1.  Staff is authenticated and able to interact with system.
2.  Staff must know targeted student�s id.

Post-condition

Health detail is edited and saved to the database.�

Main Flow

1.  Staff presses update report.
2.  System displays a list of students� reports.
3.  Staff selects a student�s report that needs to be updated.
4.  Staff makes changes to the data and presses save.
5.  The data is updated and saved into the database.

Alternative Flow

1.  Staff does not fill in required data or data format is wrong and presses save.
2.  System prompts �invalid changes� and data will not be saved.
3.  Goes back to main flow step 2.

OR

1.  Staff presses cancel instead of save.
2.  Data is not saved.
3.  Goes back to main flow step 2.

Relationship to other use cases

Will show report using view student�s wellness report when user wants to update student�s wellness report

![](TT6L_G3_SRS_files/image024.jpg)

Figure 3.�Sequence diagram for update student�s wellness report

Figure 3.16 Sequence diagram for update student�s wellness report

### 3.1.8   R7 \- System Monitoring and Logging

Table 3.17 Use case table for monitor system usage and logs

Table 3.17 Use case table for monitor system usage and logs

Section

UC-173.1.17

Name

Monitor System Usage and Logs

Author

Lee Xiang Ze

Source

System Administrator (Stakeholder)

Short Description

Admin is able to view current system usage and detailed logs of the system.

Goal

Allow staff to know system usage status and detailed logs to ensure fluency of the system.

Actor

System Administrator

Pre-condition

1.  User must be authenticated as an admin and able to interact with the system.�

Post-condition

System usage detail and logs are shown based.�

Main Flow

1.  Admin presses view system details.
2.  System usage is displayed.

OR

1.  Admin presses view logs.
2.  Logs are displayed.

Relationship to other use cases

\-Manage User Accounts and Roles (3.1.4) � Admin actions such as role changes or user creation are logged and can be viewed in this module.

![](TT6L_G3_SRS_files/image025.jpg)

Figure 3.17 Sequence diagram for monitor system usage and logs

3.2   3.2 Performance Requirements
----------------------------------

  
1\. Response Time:

●       The system shall respond to login attempts within 2 seconds under normal load.

●       Booking fitness class, health appointment or facility within 3 seconds after form submission.

●       Scheduling or cancelling a booking within 4 seconds.

●       Loading a student�s health report shall not exceed 4 seconds.

●       Loading the wellness dashboard within 5 seconds.

2\. Throughput:

●       The system shall respond to at least 300 concurrent student users without performance degradation.

●       The system shall handle 100 appointment bookings per minute.

●       Allow 20 simultaneous schedule updates from fitness and wellness staff without error or delay.

3\. Scalability:

●       Be capable of supporting up to twice the current campus population without major architectural changes.

●       The architecture shall support modular expansion to accommodate future features and load.

●       The database design must allow partitioning or sharding to handle growing datasets efficiently.

4\. Availability:

●       The system shall be available 99.5% of the time, excluding scheduled maintenance.

●       Unplanned downtime shall not exceed 2 hours per month.

�

3.3   3.3 Usability Requirements
--------------------------------

**Ease of Use**:

●       Users shall be able to log in and access their personalized dashboard within 15 seconds.

●       Users shall be able to book appointments or fitness classes in 3 clicks or fewer from the dashboard.

●       Navigation between main modules (e.g., wellness goals, notifications, resources) shall require no more than 2 clicks from the dashboard.

**Learnability**:

●       New users shall be able to complete their first appointment booking or goal setting within 5 minutes of guidance or documentation.

●       A tutorial pop-up and FAQ shall be provided on the dashboard to aid on boarding.

**Efficiency**:

●       The portal shall auto-fill repeat booking fields based on user history to reduce manual input time by 50%.

●       The system shall allow users to view and track their wellness progress in under 5 seconds.

●       Users shall be able to update their profile or preferences in fewer than 4 steps.

**Satisfaction**:

●       Users shall receive a confirmation or success message for all major actions (e.g., goal set, booking completed).

●       The platform shall include motivational feedback (e.g., badges or progress bars) for completed wellness goals.

●       The system shall support dark mode and adjustable text size for user comfort.

3.4    3.4 Interface Requirements
---------------------------------

### 3.4.1   3.4.1 System Interfaces

●       The system shall integrate with the campus�s medical system for fetching student personal data, appointment data, available appointment slots and also synchronize bookings.

●       The system shall interface with the campus fitness center�s software to retrieve and update fitness class schedules and the student enrollment.

●       All login credentials will be verified against the university�s LDAP for secure, centralized authentication.

●       The system will push reminders and health updates via a notification microservice that supports email and in-platform alerts.

### �3.4.2 User Interfaces

●       The portal shall have a responsive web interface accessible from both desktop and mobile browsers.

●       The top navigation bar shall include links to: Home, Schedule Health Appointment, Book Fitness Class, Track Wellness Progress, View Health Report, etc.

●       Students will have a personalized dashboard showing wellness points, upcoming appointments, fitness class enrollment, facility booking, notifications, tailored health resources. Form-based interaction for bookings.

●       Panel for viewing and updating student wellness reports, approving wellness goal progress, and managing appointments.

●       Interface to update facility schedules, approve student registrations and manage fitness class capacity.

●       Administrators have full access to logs, user accounts, approve student registrations, and manage fitness class capacity.

●       Admins and staff will have a role-based control panel for managing logs, updating reports and modifying facility schedules.

### 3.4.2   3.4.3 Hardware Interfaces

●       The system is web-based and does not need any special hardware.

●       The system shall support standard input/output devices, such as keyboard, mouse, and touchscreen.

●       Optional support for barcode/ QR scanners to mark attendance in physical fitness classes.

●       The platform shall be operable on standard desktop and mobile devices that support web-browsers (Windows, macOS, Android, iOS).

### 3.4.3   3.4.4 Software Interfaces

●       The system shall interact with the medical system�s API for reading and writing appointment data in a secure manner (e.g., REST API with JSON).

●       It shall interface with the Campus Fitness Center�s backend API to update fitness class schedules and availability.

●       The system will use a relational database (e.g., MySQL) for storing users, appointments, logs, and health data.

●       Internal notification microservice is responsible for pushing alerts and reminders, interfaced via REST.

### 3.4.4   3.4.5 Communications Interfaces

●       The system will use HTTPS (TLS 1.3) to encrypt all client-server communications. This ensures the secure transmission of user data, including sensitive information such as login credentials and personal health reports. All data exchanged via the web interface will be protected using this protocol to� uphold confidentiality and integrity.

●       To facilitate interaction with external systems such as the campus�s medical system and the campus fitness center, the portal will use REST APIs over HTTP. These APIs will allow the system to retrieve appointment schedules, update bookings, and sync health-related data using standardized JSON-formatted requests and responses.

●       The portal will use the Simple Mail Transfer Protocol (SMTP) to send emails to students. These emails will include appointment confirmations, fitness class reminders, and notifications related to goal progress or system activity. The system will connect to the campus�s email infrastructure or an authorized SMTP service provider to perform this function securely and reliably.

3.5   3.5 Logical Database Requirements
---------------------------------------

The �WellnessGoal� entity has attributes such as goalId, description and progress, and it has a composition relationship with the �Student� entity.

The �User� entity has attributes such as userId, name, email and password, and it has methods such as login() and logout(). It is the parent class of �Student�, �SystemAdministrator�, �WellnessStaff� and �FitnessStaff� entities.

The �Notification� entity has attributes such as notificationId, message and timeStamp, and it has methods such as sendNotification(student : Student). It has an aggregation relationship with the �Student� entity.

The �Student� entity has attributes such as wellnessPoints and goals, and it has methods such as bookAppointment(), bookClass(), bookFacility(), trackProgress(), redeemPrize(), cancelAppointment(), rescheduleAppointment(), setWellnessGoal() and viewHealthReport(). It is the child class of the �User� entity and it has the aggregation relationships with �Notification�, �Appointment�, �FitnessClass�, �Facility� and �WellnessReport� entities.

The �SystemAdministrator� entity has methods such as monitorLog() and manageUsersAndRoles(). It is the child class of the �User� entity and it has an association relationship with the �SystemLog� entity.

The �WellnessStaff� entity has methods such as viewWellnessReport(), updateWellnessReport() and manageAppointment(). It is the child class of the �User� entity and it has an association relationship with the �Appointment� class.

The �FitnessStaff� entity has methods such as manageClassSchedule(), manageFacility(), viewWellnessReport() and updateWellnessReport(). It is the child class of the �User� entity and it has the association relationships with �FitnessClass�, �Facility�, and �WellnessReport� entities.

The �SystemLog� entity has attributes such as logId, activity and timeStamp. It has an association relationship with the �SystemAdministrator� entity.

The �Appointment� entity has attributes such as appointmentId, dateTime, location and status. It has association relationships with �Student� and �WellnessStaff� entities.

The �FitnessClass� entity has attributes such as classId, name and schedule. It has association relationships with �Student� and �FitnessStaff� entities, and has a composition relationship with the �Schedule� entity.

The �Facility� entity has attributes such as facilityId, name and availability. It has association relationships with �Student� and �FitnessStaff� entities, and has a composition relationship with the �Schedule� entity.

The �WellnessReport� entity has attributes such as reportId, studentId and healthMetrics. It has association relationships with �Student�, �WellnessStaff� and� �FitnessStaff� entities.

The �Schedule� entity has attributes such as startTime, endTime and dayOfWeek. It has composition relationships with �FitnessClass� and �Facility� entities.

![](TT6L_G3_SRS_files/image026.gif)

Figure 3.19 Class diagram

Figure 3.19 Class diagram

3.6   3.6 Design Constraints
----------------------------

The system design must comply with the university�s brand guidelines, such as the use of official colors, logos, and fonts in all user interface components. The software requirements and development processes need to follow the IEEE/ISO/IEC 29148-2018 standard, because it offers a structured approach to defining, documenting and managing requirements, which can lead to a better project outcome and better customer satisfaction with a lower risk. In addition, to help ensure the system is usable by the people with diverse abilities, the system must be accessible according to WCAG 2.1 AA standards. Moreover, all user data management processes must comply with data privacy regulations such as the Personal Data Protection Act (PDPA) to prevent any form of abuse against the storage or processing of personal data of individuals. The technical limitations include the support for legacy hardware in offices for staff and compliance with internal IT security policies such as routine audits and controlled deployment processes within the institution�s scheduled maintenance windows.

3.7    3.7 Software System Attributes
-------------------------------------

### 3.7.1   3.7.1 Reliability

The system should recover automatically from crashes or service interruptions within 1 minute using checkpointing and failover mechanisms. Additionally, transactional integrity should be preserved for health appointments and class bookings even when unexpected failures.

In cases of third-party API downtime, the system activates a queuing mechanism and stores temporary data in a local cache. Once the API is available again, pending updates are pushed. Administrative users are alerted when synchronization fails, enabling them to monitor and ensure data integrity during outages.[\[N6\]](#_msocom_6) 

### 3.7.2   3.7.2 Availability

The system should maintain an operationaloperational availability of 99.5% during the ongoing semester period. Scheduled maintenance must be announced at least 24 hours in advance and avoid peak usage period.

### 3.7.3   3.7.3 Security

The system is implemented with Role-Based Access Control (RBAC) to verify the access rights are given based on roles of the users. Students, wellness staffs, fitness staffs and administrators all possess clearly defined scopes of access. As an example, fitness staff can only have access to fitness-based measures.

Every in-transit data is encrypted with AES-256 and HTTPS. In the case of administrative operations, like updating the account or changing the schedule, an administrator can log all the changes, including timestamp, user ID and description of the change. These logs are stored safely on the company standards of audit.Role-based access control (RBAC) should be implemented for students, system administrator, wellness staff and fitness center staff. All user data in transit must be encrypted using AES-256 and the website should be secured with HTTPS. Additionally, the system must be protected against cross-site scripting (XSS), SQL injection and session hijacking. 2FA should be mandated for administrative access. All the changes regarding administrative purpose will be logged for tracebacks.

### 3.7.4   3.7.4 Maintainability

The system should follow modular design principles and separation of concerns to isolate components such as UI, backend logic and third-party API integration. Therefore, Object-oriented concepts using MVC (Model View Controller) method must be obeyed while designing the system. The codebase should be written using clean code principles and fully documented to support maintainability and onboarding of new developers. Interfaces between modules should be standardized using API versioning to minimize refactoring impact.

### 3.7.5   3.7.5 Portability

The software shall be deployed on both Linux and Windows-based servers with no major configuration changes. Only 5% of the total codebase should be allowed as host-dependent code. The system shall be developed in portable language stack such as Python Flask and JavaScript to avoid the use of OS-specific dependencies. Container-based deployment should be supported for portability across cloud and on-premise environments.�

3.8   3.8 Supporting Information
--------------------------------

(Mapped to 9.6.20 Supporting Information)

Any additional supporting information, including:

a)�� sample input/output formats, descriptions of cost analysis studies or results of questionnaires or any other elicitation techniques;

b)� supporting or background information that can help the readers of the SRS;

c)�� a description of the problems to be solved by the software; and

d)� special packaging instructions for the code and the media to meet security, export, initial loading or other requirements.

The SRS should explicitly state whether or not these information items are to be considered part of the requirements.

Example:

Sample input/output formats for key system functions (e.g., CSV format for data export).

### 3.8.1    3.8.1 Sample Input/Output Formats & Supporting Artifacts

**Sample Input/Output Formats:**

●       Book health appointment

○       Input: JSON format

{

� "student\_id": "1211105123",

� "appointment\_type": "Medical Checkup",

� "date\_time": "2025-05-20 09:30",

� "status": "Confirmed"

}

○       Output: Confirmation message in JSON

{

� "status": "Confirmed",

� "appointment\_id": "A0131",

� "date\_time": "2025-05-20 09:30",

� "location": "FCI-CQCR2003"

}

●       Book fitness class

○       Output: CSV format

Class\_ID, Class\_Name, Student\_ID, Booking\_Status

FCI6261, Yoga, 1211105123, Enrolled

FCI6351, Zumba, 1211106321, Waitlisted

**Elicitation Techniques Used:**

●       Brainstorming Session

\-        Help to identify existing system gaps, essential user roles and privileges.

\-        Conducted a Microsoft Team meeting where participants could quickly share ideas.

\-        Link of the recording for brainstorming meeting:

[Recap: Meeting 2 for SRE Project Part 1 Tuesday, 29 April](https://teams.microsoft.com/l/meetingrecap?driveId=b%21uA3ock664EigZAz7spXQQkB3wwZxBhdNvTdZdP_c4JlZcIIe3dnTSbNzKVpSZppB&driveItemId=01IIE4OSFKRKAJKF3M2FDYH5LJO3R3LGPZ&sitePath=https%3A%2F%2Fmmuedumy-my.sharepoint.com%2F%3Av%3A%2Fg%2Fpersonal%2Fng_jin_mun_student_mmu_edu_my%2FEaqKgJUXbNFHg_VpduO1mfkBAy7l3ptuSGIM-Gyfk5vYZQ&fileUrl=https%3A%2F%2Fmmuedumy-my.sharepoint.com%2Fpersonal%2Fng_jin_mun_student_mmu_edu_my%2FDocuments%2FRecordings%2FMeeting%25202%2520for%2520SRE%2520Project%2520Part%25201-20250429_200258-Meeting%2520Recording.mp4%3Fweb%3D1&iCalUid=040000008200e00074c5b7101a82e00800000000b4a4c84dccb8db010000000000000000100000001ebe461c29c053439e176d67e367b68d&threadId=19%3Ameeting_MWMxMmQ3ODktNTQ0ZS00NTIzLTkwYWItOGJlYzFlZDZjNzJm%40thread.v2&organizerId=49f8112a-4f7e-4620-9782-713819f9f993&tenantId=7e0b5fcf-12c4-4eff-96b6-4664f25dc7da&callId=f0c89d5c-f00a-4e22-b93d-f4175d8baacf&threadType=Meeting&meetingType=Scheduled&subType=RecapSharingLink_RecapCore)

![](TT6L_G3_SRS_files/image027.jpg)

Figure 3.20 Microsoft Teams Meeting Attendance Page

Figure 3.20 Microsoft Teams Meeting Attendance Page

  

●       Questionnaires

\-        Distributed to a sample of stakeholders to understand the user expectation about system requirements.

\-        Below are the results of **functional requirement** from our questionnaire:  
  

**1.**    **Book health appointment**

**![Forms response chart. Question title: How would you feel if you could book medical appointments online through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image028.gif)**

Figure 3.21 Questionnaire Chart Diagram 1

Figure 3.21 Questionnaire Chart Diagram 1

It is clear in the chart that most of the users (65%) want to have an option of booking medical visits online via the portal showing a high degree of acceptance towards the feature. Moreover, 20 percent assume it, implying that it is now considered to be a norm in current computerized set-up. No respondent reported disliking it with 5 stating that they could live with and 10 saying that they are neutral to the idea, it appears that there is no resistance to the idea with no aversion on the other side. In general, the feedback is very positive given that the majority of the users are either favoring or anticipating the feature which affirms its significance to be part of the wellness portal.

**![Forms response chart. Question title: How would you feel if you could NOT book medical appointments online through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image029.gif)**

Figure 3.22 Questionnaire Chart Diagram 2

Figure 3.22 Questionnaire Chart Diagram 2

This clear in the chart, that when online medical appointment booking is not done through the portal, 45 percent of the respondents will be okay undergoing it, 30 percent were neutral meaning, they were tolerating it but not excited. But 20 percent would not like it because the feature is not therethere, and 5 percent do anticipate it showcasing a significant rate of dissatisfaction or unmet expectations. Even though almost a half of them could accept that they would not get the feature, a total of 25 percent consider it as a loss, strengthening that online booking is turning into a valued or expected service.

**2.**    **View health report**

**![Forms response chart. Question title: How would you feel if you could access your personal medical history online through the portal? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image030.gif)**

Figure 3.23 Questionnaire Chart Diagram 3

Figure 3.23 Questionnaire Chart Diagram 3

The chart indicates that 50 percent (50%) of the respondents would appreciate having the capability to view their own medical history online via the portal with the remaining 15 percent expecting the same, which is a clear indication that most of the users are interested and would require the capability in the future. Moreover, 25 would be neutral, and fewer groups (5% each) would live with or dislike it. All in all, the findings show that the majority of users regard this feature as quite valuable, which makes it possible to introduce the possibility of accessing medical history online as an essential aspect of the portal.

**![Forms response chart. Question title: How would you feel if you could NOT access your personal medical history online through the portal? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image031.gif)**

Figure 3.24 Questionnaire Chart Diagram 4

Figure 3.24 Questionnaire Chart Diagram 4  
The chart demonstrates that 50 percent of respondents would give preference to the possibility of receiving their personal medical history online via the portal, 15 percent would sense it, and these are quite indicative figures, which proves the interest and increasing users to explore and approach this option. Moreover, 25 percent have no opinion, smaller percentages (5 each) would live with it or not like it. All in all, the findings indicate that the majority of the users perceive this functionality as of a great value, which made it possible to envisage online-based access to the medical history as an important part and parcel of the portal.

**3.**    **Online doctor consultation**

**![Forms response chart. Question title: How would you feel if you could consult with a doctor online through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image032.gif)**

Figure 3.25 Questionnaire Chart diagram 5

Figure 3.25 Questionnaire Chart diagram 5

According to the chart, the potential of online consultation with a doctor by means of the portal is very high as 60 percent of those surveyed desire that possibility, and one more 15 percent think that it will be available, which means big demand and increasing expectations regarding teleconsultation. In the meantime, 10 percentagepercent engage in-between, and a minor group (10 percentagepercent) would hate it, as 5 percentagepercent claim they would learn to live with it. Such appreciation in general would indicate the feasibility of offering online doctor consultations within the portal as something that would be positively accepted and follow the needs of users concerning the convenience and accessibility.

**![Forms response chart. Question title: How would you feel if you could NOT consult with a doctor online through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image033.gif)**

Figure 3.26 Questionnaire Chart diagram 6

Figure 3.26 Questionnaire Chart diagram 6

The chart indicates that in case of not having online doctor consultations in the portal, forty percent of the users would put up with it only and thirty fivethirty-five percent would be neutral, thus moderate acceptance of not having it. Nonetheless 15 percent would want the feature, 5 percent would be anticipating it, and 5 percent would not be pleased atwith its absence. Even though a large portion of users can agree to lack online consultations, a significant proportion of them shows verya very specific desire or anticipation of such presence, which indicates that introducing such a feature would result into higher users satisfaction and modernization of portal guidance in the platform in terms of healthcare.

**4.**    **Book fitness class**

**![Forms response chart. Question title: How would you feel if you could book fitness classes (Yoga, Zumba, etc.) online through the portal? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image034.gif)**

Figure 3.27 Questionnaire Chart diagram 7

Figure 3.27 Questionnaire Chart diagram 7

The chart indicates that the online fitness class booking on the portal has an enormous support whereby 70 percent of respondents responded that they would like it and another 10 percent expect it which is an indication of the very high user demand. In the meantime, 10 percent of the respondents keep themselves neutral, and on the one hand, only 5 percent of them say they would just live with it, and 5 percent suggests they would not like the feature. The high preference also indicates that inclusion of the fitness class booking regime to the portal would greatly increase user friendliness and interaction.

**![Forms response chart. Question title: How would you feel if you could NOT book fitness classes (Yoga, Zumba, etc.) online through the portal? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image035.gif)**

Figure 3.28 Questionnaire Chart diagram 8

Figure 3.28 Questionnaire Chart diagram 8

The chart shows that without online booking of fitness classes, 45 percent of the participants would neither agree nor disagree, whereas 20 percent would live with it, which implies a moderate level of the option. Nevertheless, 15 percent of them would demand it and 15 percent would not appreciate being without this capability so there is a significant minority who considered this to be either a necessity or that it is so desirable they would demand it. These findings emphasize that although there would be tolerance of not having this feature, the fact is that a significant portion of the users would insist or desire that the feature be present on the portal.

**5.**    **Track fitness progress**

**![Forms response chart. Question title: How would you feel if you could track your fitness progress through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image036.gif)**

Figure 3.29 Questionnaire Chart diagram 9

Figure 3.29 Questionnaire Chart diagram 9

The chart demonstrates the fact that 60 percent of the respondents would enjoy the possibility to monitor their fitness level with the help of the portal, whereas 20 percent of the respondents anticipate this possibility, which indicates that the users are capable of interest in and appreciate this feature to a significant degree. In the meantimemeantime, 10 percent said they are neutral and the remaining 10 percent would not like it with little opposition. In aggregate, it is noticeablenoticeable that the great interest and anticipation to the feature of fitness tracking which is supposed to make a significant contribution to the user experience and commitment inside the wellness portal.

**![Forms response chart. Question title: How would you feel if you could NOT track your fitness progress through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image037.gif)**

Figure 3.30 Questionnaire Chart diagram 10

Figure 3.30 Questionnaire Chart diagram 10

The chart indicates that almost 55 percent of the respondents would remain neutral in case they could not track their progress at fitness training in the portal, with 20 percent being all right with it, as they are generally tolerant. Nonetheless, 15 percent would not like it to be missing with a mere 5 percent saying that they would like the feature, or want it. Even though the absence of this feature may not be a big concern of most users, the existence of users who would have noticed or at least expected it to be there bolsters the idea of the addition of fitness tracking capability to boost user interest and health tracking.

**6.**    **Redeem prize**

**![Forms response chart. Question title: How would you feel if you received rewards (e.g., fitness accessories, vouchers) for achieving fitness goals through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image038.gif)**

Figure 3.31 Questionnaire Chart diagram 11

Figure 3.31 Questionnaire Chart diagram 11

The graph presents an overwhelming majority of support of receiving rewards when meeting fitness goals in the portal, with 70% of people answering that it would be desired and 20% expecting it as a great motivator and interest in incentivized health. A mere 10 percent are neutral and no one dislikes or disapproves. The answer makes it clear that the use of a reward system would be a very involving and rewarding addition to the system, which would inculcate an increased sense of participation and achievement.

**![Forms response chart. Question title: How would you feel if you did NOT receive rewards (e.g., fitness accessories, vouchers) for achieving fitness goals through the portal?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image039.gif)**

Figure 3.32 Questionnaire Chart diagram 12

Figure 3.32 Questionnaire Chart diagram 12

The chart shows that in the event of the portal failing to reward users upon fulfilling the fitness objectives, half (50%) of users would be neutral and 25 percent would be able to live with it, which implies overall acceptance to the issue. Nevertheless, 15 percent of them would not like the lack of reward, and 10 percent would not expect them. Although the non-remuneration factor might not be catastrophic to the majority, a substantial number of them appreciate awards therefore it is important to mention that addition of some rewards can do wonders in motivation and general participation.

**7.**    **Receive tailored health resource**

**![Forms response chart. Question title: How would you feel if the portal provided personalized wellness tips (nutrition, exercise, mental health)?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image040.gif)**

Figure 3.33 Questionnaire Chart diagram 13

Figure 3.33 Questionnaire Chart diagram 13

It is reported on the chart that 60 percent of those inquired would prefer to receive individualized wellness advice by nutrition, exercise, and mental health via the portal and another 20 percent would anticipate that. This is a solid preference with increasing demands. The rest of 20 percent are neutral, and no person disliked or reported disliking. This proves that customized wellness suggestions would be exceedingly appreciated and favored, and that would probably result in greater user experience and interaction with the portal.

**![Forms response chart. Question title: How would you feel if the portal did NOT provide personalized wellness tips (nutrition, exercise, mental health)?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image041.gif)**

Figure 3.34 Questionnaire Chart diagram 14

Figure 3.34 Questionnaire Chart diagram 14

Based on the chart, the absence of individual wellness advice would make 55 percent of the respondents indifferent and 10 percent live with it, which means something of an indifference or tolerance. Nevertheless, 30 percent of them would not appreciate this feature and 5 percent would even anticipate it. This implies that the absence of personalized tips would be acceptable to many users but a considerable part of them would get disappointed, so the feature should enhance the value to the user experience of the wellness portal.

**8.**    **VR fitness session**

**![Forms response chart. Question title: How would you feel if the portal offered VR fitness sessions (e.g., virtual yoga or guided workouts using VR headsets)? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image042.gif)**

Figure 3.35 Questionnaire Chart diagram 15

Figure 3.35 Questionnaire Chart diagram 15

As the chart indicates, 60 percent of the people would welcome the concept of VR fitness classes, via the portal because 5 percent anticipate it and 25 percent are neutral, which implies a lot of interest and interest or openness to the capability. Only a fifth would live with it and other fifth would not like it. These findings imply that though it is not a prior necessity, VR activities of the fitness form would be an exciting and creative option that many users would enjoy, and one that can lead to boosting the interaction and updating the wellness.

**![Forms response chart. Question title: How would you feel if the portal did NOT offer VR fitness sessions (e.g., virtual yoga or guided workouts using VR headsets)? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image043.gif)**

Figure 3.36 Questionnaire Chart diagram 16

Figure 3.36 Questionnaire Chart diagram 16

The chart demonstrates that 65% of the respondents will remain rather indifferent that the portal does not provide VR fitness classes so that most of the users will not care whether this feature is available or not. In the meantime, 10 percent of these would anticipate it, such as its non appearancenon-appearance, toleratetolerating its existence or hate its absence. These ambivalent reactions imply that VR fitness is no more than an additional feature that some users will also find appealing but not an aspect that would need to remain a priority.

\-        Here are the results of each **quality requirement** from our questionnaire method:  
  
**1. System Availability**  
![Forms response chart. Question title: If the system will be available 99.5% of the time, how would you feel? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image044.gif)

Figure 3.37 Questionnaire Chart diagram 17

Figure 3.37 Questionnaire Chart diagram 17

The chart gives a good indication of the level of reliability expected of the system by the people responding saying that 80 percent expect the system to be available 99.5 percent of the time. In the mean timemeantime, 10 percent are desirous of this degree of availability and 10 percent remain neutral. This reply is an indication of the strong belief that system uptime has become a prerequisite, and not an option, and it is necessary to ensure that it is highly available, just to satisfy the expectations of users.

  
  

![Forms response chart. Question title: If the system will NOT be available 99.5% of the time, how would you feel? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image045.gif)

Figure 3.38 Questionnaire Chart diagram 18

Figure 3.38 Questionnaire Chart diagram 18

This figure in the chart is clear that 85 percent of the respondents would not like the system not to work 99.5 percent of the time, and this is the degree to which having a system up all the time matters to users. Just 1 in 10 feel neutral and just a paltry 1:20 anticipate such lowa low supply. These findings are very strong with the assertion that high availability is not a choice, it is a necessity to user satisfaction and trust on the system.

**2\. System Responsiveness**

![Forms response chart. Question title: If the response time for user actions is under 3 seconds, how would you feel? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image046.gif)

Figure 3.39 Questionnaire Chart diagram 19

Figure 3.39 Questionnaire Chart diagram 19

It indicates that 75 percent of the respondents prefer to use the system that would respond within 3 seconds, which underlines affinity towards quick and efficient performance. In the meantime, 10 percent would want such speed to be the case, 10 percent are neutralneutral, and 5 percent would be able to put up with it. The findings imply that the responsiveness of the system is a significant quality attribute to the portal as it plays significant roles in user satisfaction due to the fast response time.

![Forms response chart. Question title: If the response time for user actions is NOT under 3 seconds, how would you feel? . Number of responses: 20 responses.](TT6L_G3_SRS_files/image047.gif)

Figure 3.40 Questionnaire Chart diagram 20

Figure 3.40 Questionnaire Chart diagram 20

In the chart, it comes out that 9 out of 10 respondents would not like response time to take more than 3 seconds, a fact that shows the high value of speed to the user experience. An equal majority of respondents (90 percent) are against slower performance and only 10 percent are neutral. Indifferent or positive results were not registered. This tidal wave of disapproval points at the fact that anything longer than 3 seconds is not acceptable to users, and hence responsiveness is not a matter of choice to the system.

**3\. Data Protection**

![Forms response chart. Question title: If your data is protected under Personal Data Protection Act 2010 (PDPA) to ensure privacy, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image048.gif)

Figure 3.41 Questionnaire Chart diagram 21

Figure 3.41 Questionnaire Chart diagram 21

According to the chart, majority of the respondents (75 percent) would wish their information to be secured under the Personal Data Protection Act 2010 (PDPA), 15 percent have anticipated it, five percent are indifferent, and another five percent could bear with it. Such high priority for protection and secrecy of data could promote the role of data and privacy protection to users which brings in a sign that PDPA-compliant systems will not only increase user confidence and trust, buttrust but will also raise user satisfaction with the system.

![Forms response chart. Question title: If your data is NOT protected under Personal Data Protection Act 2010 (PDPA) to ensure privacy, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image049.gif)

Figure 3.42 Questionnaire Chart diagram 22

Figure 3.42 Questionnaire Chart diagram 22

According to the chart, eighty five out of one hundred percent of respondents would not like their information not to be gleaned in the Personal Data Protection Act 2010 (PDPA) and this explains in clear terms that privacy in data and legal compliance is critical. Only in 10% and expectation of protection feels 5 percent of people, and nobody states indifference or approval. This grievous preoccupation gives credence to the fact that PDPA compliance cannot be optional, but a necessary step towards credible user faith and credibility.

**4\. Conveniency**

![Forms response chart. Question title: If the booking procedures are able to be done within 3 clicks, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image050.gif)

Figure 3.43 Questionnaire Chart diagram 23

Figure 3.43 Questionnaire Chart diagram 23

The chart shows that 75 percent of the respondents are neutral concerning the booking procedures being fulfilled in 3 clicks and 15 percent would like it, 5 percent expect it and 5 percent would not like it. Most users do not care; however, the fact that a significant part responded positively means that by streamlining the process of booking and making it fast and simple, one could still improve the overall and more customer-friendly experience.

![Forms response chart. Question title: If the booking procedures are NOT able to be done within 3 clicks, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image051.gif)

Figure 3.44 Questionnaire Chart diagram 24

Figure 3.44 Questionnaire Chart diagram 24

The chart indicates that 85 percent of respondents would certainly not like it that the booking procedures could not be easily done in 3 clicks, which implies that there is a very high rate of user demand of speed and simplicity. Just 10 percent are neutral and 5 percent can live having to put up with the inconvenience. This is such an adverse response that highlights that zero-click-count booking process is key to good user experience on the portal.

**5\. Consistent Update**

![Forms response chart. Question title: If the system receives regular feature updates and bug fixes with minimal downtime, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image052.gif)

Figure 3.45 Questionnaire Chart diagram 25

Figure 3.45 Questionnaire Chart diagram 25

According to the chart, 75 percent of the respondents would prefer frequent updates of the features and fixing bugs that have minimal downtime, 10 percent expected it and 10 percent were neutral. Just 5 percent would accept to live with it and no one indicated to hate it. It reveals a definite user-preference toward the continuous improvement and stability of the system as the normal updates and re-balance prove to be not only welcome, but also increase the levels of trust and contentedness with the portal.

![Forms response chart. Question title: If the system NOT receives regular feature updates and bug fixes with minimal downtime, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image053.gif)

Figure 3.46 Questionnaire Chart diagram 26

Figure 3.46 Questionnaire Chart diagram 26

It is indicated in the chart that a majority (65 percent) of the respondent will anticipate that the system should be updated regularly with fixes on bugs and 25 percent will not like it when this is not the case which goes in to show how important the maintenance regularly is to the users. It is the lowest at only 10 % who are neutral. These answers give a clear picture that the users consider the trend of improvements and zero-tolerance to downtimes as a minimum, and its non-achievement can considerably reduce satisfaction and confidence towards the system.

**6\. Portability**

![Forms response chart. Question title: If the system works smoothly across mobile, desktop, and different browsers, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image054.gif)

Figure 3.47 Questionnaire Chart diagram 27

Figure 3.47 Questionnaire Chart diagram 27

Most of the respondents (65%) would be comfortable with the functionality of the system on mobile, desktop and different browsers; 15 percent are neutral and only 10 percent each like or would expect it. This will mean that the cross-platform compatibility is not only something liked, but users will find it to be a standard or something to be expected. The cross-device performance remains necessary to secure a smooth experience among the devices, but it will not be sufficient to raise the user satisfaction in a remarkable way unless the issues occur.

![Forms response chart. Question title: If the system NOT works smoothly across mobile, desktop, and different browsers, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image055.gif)

Figure 3.48 Questionnaire Chart diagram 28

Figure 3.48 Questionnaire Chart diagram 28

Based on the graph, 85 percent of the respondents would not like it that the system was not working cleanly across mobile, desktop, and different browsers whereas the other 15 percent have no feeling. Such widespread displeasure emphasizes that cross-platform compatibility is an extremely important requirement of the user and its deviation in this regard would not do immense favors to the general user experience and the credibility of the system.

**7\. System Reliability**

![Forms response chart. Question title: If the system does not down within peak usage, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image056.gif)

Figure 3.49 Questionnaire Chart diagram 29

Figure 3.49 Questionnaire Chart diagram 29

The chart indicates that 75 percent respondents have a neutral attitude to the fact that the system is not going down under heavy usage, 15 percent would prefer it, 5 percent would anticipate it and another 5 percent would not like it. Most users seem to be uninterested but the existence of positive expectations implies that the stability of the system when there are high demands is welcomewelcome, and it influences user confidence when utilizing the certainty of the system.

![Forms response chart. Question title: If the system down within peak usage, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image057.gif)

Figure 3.50 Questionnaire Chart diagram 30

Figure 3.50 Questionnaire Chart diagram 30

According to the chart, eighty five percent of the respondents would not like system downtime when systems are most used and fifteen percent are neutral. The resultant expression of such hatred is accentuated by the fact that stability of systems facing elevated traffic is important. Any failure to perform during those moments would majorly destroy user trust and satisfaction and uptime during peak usages will be high operations priority.

**8\. Learnability**

![Forms response chart. Question title: If the system pop-up tutorial and FAQ for the first-time users, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image058.gif)

Figure 3.51 Questionnaire Chart diagram 31

Figure 3.51 Questionnaire Chart diagram 31

On the chart, 80% of the respondents would like a pop-up tutorial and FAQ to use when the user is using the product the first time, and so planning onboarding assistance has a wide range of supporters. In the meantime, 10% are anticipating it, 5% are neutral and 5% can live with it. These findings indicate that giving understandable and familiar instruction is of importance and immensely would enhance the usability and friendliness of the system to new users.

![Forms response chart. Question title: If the system does not pop-up tutorial and FAQ for the first-time users, how would you feel?. Number of responses: 20 responses.](TT6L_G3_SRS_files/image059.gif)

Figure 3.52 Questionnaire Chart diagram 32

Figure 3.52 Questionnaire Chart diagram 32

The chart indicates that, 75 percent of the respondents would be indifferent in the event that the system is devoid of a pop- up next tutorial and frequently asked questions by first-time users whereas 20 percent would detest its absence and 5 percent could live with it. Most users do not express their feelings, but the significant share of them say that they do not like onboarding tools, which also means that onboarding tools are primarily necessary to enhance the first-time user experience and mitigate the confusion.

**Final result:**

The table below shows the Kano category of each final requirement after interpreting the actual results based on the percentage responses from the questionnaire:

Table 3.18 Final Requirements Table

Table 3.18 Final Requirements Table

**Requirement**

**Kano Category**

**Requirement Type**

**Justification**

**Technique**

Log in

Dissatisfier

Functional

Essential for access

Brainstorming

Manage user accounts and roles

Dissatisfier

Functional

Required for system control

Brainstorming

Monitor system usage and logs

Dissatisfier

Functional

Important for maintenance

Brainstorming

Book health appointment

Delighter

Functional

Improves user experience

Brainstorming,QuestionnaireBrainstorming, Questionnaire

Book fitness class

Delighter

Functional

Convenience for users

Brainstorming,QuestionnaireBrainstorming, Questionnaire

Book facility

Delighter

Functional

Improves user experience

Brainstorming,QuestionnaireBrainstorming, Questionnaire

Receive notification

Satisfier

Functional

Enhances usability

Brainstorming

View health report

Delighter

Functional

Adds value for users

Brainstorming, Questionnaire

Cancel/ Reschedule appointment

Dissatisfier

Functional

Basic functionality

Brainstorming

Receive tailored health resource

Delighter

Functional

Personalize experience

Brainstorming,QuestionnaireBrainstorming, Questionnaire

Track wellness progress

Delighter

Functional

Motivates users

Brainstorming,QuestionnaireBrainstorming, Questionnaire

Set wellness goal

Satisfier

Functional

Encourages goal setting

Brainstorming

Redeem prize

Delighter

Functional

Rewards engagement

Brainstorming,QuestionnaireBrainstorming, Questionnaire

Manage facility

Dissatisfier

Functional

Management access

Brainstorming

Manage fitness class schedule

Dissatisfier

Functional

Needed for coordination

Brainstorming

View student�s wellness report

Dissatisfier

Functional

Required for monitoring

Brainstorming

Update student�s wellness report

Dissatisfier

Functional

Required for updates

Brainstorming

Manage Appointment

Dissatisfier

Functional

Core system requirement

Brainstorming

System Availability

Dissatisfier

Quality

Ensure accessible of the system

Brainstorming,

Questionnaire

System Responsiveness

Satisfier

Quality

Ensure feedback to user request

Brainstorming,

Questionnaire

Data Protection

Satisfier

Constraints

Ensure regulation to country�s law regarding to personal data

Brainstorming,

Questionnaire

Conveniency

Dissatisfier

Quality

Ensure ease to perform desired functionality

Brainstorming,

Questionnaire

Consistent Update

Delighter

Quality

Ensure regular update to fix bugs and improvements

Brainstorming,

Questionnaire

Portability

Dissatisfier

Quality

Ensure system to be able to accessed in various platforms

Brainstorming,

Questionnaire

System Reliability

Dissatisfier

Quality

Ensure system does not break down when high traffics

Brainstorming,

Questionnaire

Learnability

Delighter

Quality

Ensure knowledge on accessing core functionalities

Brainstorming,

Questionnaire

### 3.8.2    3.8.2 Supporting or Background Information

The Campus Wellness Portal was introduced in response to increasing demand for a centralized platform that supports student well-being through seamless access to health and fitness services. In the past, students were facing the problems that fragmented systems for booking medical appointments and fitness activities brings, such as missed opportunities, insufficient scheduling and low engagement with wellness programs. This system can help to achieve the university�s goal, which is promoting overall student wellness, combined with rising concerns over mental and physical health in academic settings. By integrating the medical system and fitness center into one cohesive portal, it could streamline the access, reducing management burden and promoting a healthier campus lifestyle. This is why the features such as role-based access, real-time booking, goal tracking and cross-system integration are prioritized in the system requirements.

### 3.8.3    3.8.3 Problems to be solved by the Software

Due to the fragmentation of the systems, students are facing inconvenience to manage their health and wellness. The medical appointment and fitness class bookings are typically handled through a separate system, where each of them have their own login, interface and limitations. This causes students to miss their appointments, underutilization of wellness programs, easy to conflict with schedules and overall disengagement from proactive health management. Additionally, the system administrator needs to maintain multiple different systems, leading to the inefficiency of handling manual coordination and managing user access securely. Due to the lack of centralized oversight, the ability of university to monitor user patterns, spot service gaps and implementation of data-driven improvement is limited. By integrating with the medical system and fitness center, the Campus Wellness Portal could solve these issues by providing a centralized, user-friendly system that streamlines scheduling and tracking, enhances engagement and improves operational efficiency across wellness-related departments.

### 3.8.4    3.8.4 Special Packaging Instructions

Firstly, for initial deployment and loading, the software should be packaged as a Docker container image with associated �docker-compose.yml� files for simplified deployment across deployment, testing and production environments. Database schema and seed data should be included in an ORM-compatible migration tool (SQLAlchemy) and encrypted archive (AES-256 encrypted ZIP). For exporting and distributing consideration, as this system includes medical and personal wellness data encryption modules, it will include TLS 1.3 and AES-256 for data in transit and data at rest. Integrity validation will be using HMAC. A strict review will be conducted to ensure the system regulates the Personal Data Protection Act 2010 (PDPA). Additionally, all deliverables shall be digitally signed using the university�s official GPG/PGP keys to ensure integrity and authenticity. If physical transport is required, software should be stored on hardware-encrypted USB drives compliant with institutional standards such as the FIPS 140-2. Hash checks using SHA-256 and digital signature verification must be performed prior to installation. For the deployment package, it must include source code and container image, environment setup and rollback scripts, documentation for administrators and auditors, encrypted credentials, data privacy and compliances notes. Lastly, all sensitive values such as database passwords, signing keys, third-party tokens shall be excluded from the package and managed securely using runtime secret injection methods. The initial deployment process must also require manual credential initialization and enforced password change. Initial setup of TLS certificates and API key rotation as well as audit logging configuration are required.

  

### 3.8.5   Validation Session

**Session ID**

**Date and Time**

**Technique**

**Section Reviewed**

**Participant & Role**

**No. of Defect**

**VS-01**

3:00 P.M. - 5:00 P.M. 14/06/2025

Inspection

1.0 - 3.3

Ng Jia Hong \[Inspector, Validator (Documentation, Content, Agreement), Organizer, Minute-Taker\] Lee Ken Yu \[Inspector, Validator (Documentation, Content, Agreement)\] Danish Haziq Inspector, Validator (Documentation, Content, Agreement)\]

17

**VS-02**

10:00 P.M. - 12:00 P.M. 16/06/2025

Inspection

3.4 - 5.3

Ng Jia Hong \[Inspector, Validator (Documentation, Content, Agreement), Organizer, Minute-Taker\] Lee Ken Yu \[Inspector, Validator (Documentation, Content, Agreement)\] Danish Haziq Inspector, Validator (Documentation, Content, Agreement)\]

13

**VS-03**

10:00 P.M. - 12:00 P.M. 20/06/2026

Commenting Artefacts

1.0 - 5.4

Ng Jia Hong \[Inspector, Validator (Documentation, Content, Agreement), Organizer, Minute-Taker\] Lee Ken Yu \[Inspector, Validator (Documentation, Content, Agreement)\] Danish Haziq Inspector, Validator (Documentation, Content, Agreement)\]

6

### 3.8.6   Defect Summary

**A. Content Defect**

**Req ID**

**Validation and Defect Description**

**Detected By**

**Comment/Suggested Fix**

**Session ID**

**Severity (1�5)**

**C-01**

Missing version control log

Ng Jia Hong

Include version history table to trace the changes between SRS versions

VS-01

3

**C-02**

No traceability matrix linking features to goals

Ng Jia Hong

Add matrix connecting use cases to objectives, actors and system capabilities

VS-01

4

**C-03**

No list for diagrams and tables

Lee Ken Yu

Include the list of diagrams and list of tables.

VS-01

2

**C-04**

No flow between Student and Campus Wellness Portal related to "Redeem prize"

Lee Ken Yu

Add "Prize redemption request" and "Redemption confirmation" flows.

VS-01

3

**C-05**

Phrases are grammatically incorrect and inconsistent.

Lee Ken Yu

Standardize format to make message clearer, should be: �Prompt: Slot updated successfully�.

VS-01

2

**C-06**

Inconsistent Conditional Label

Ng Jia Hong

Should be �Return if user exists�.

VS-01

3

**C-07**

Potential misleading title at Cancel/Reschedule Appointment

Danish Haziq

Correct the use case description to refer to health appointment cancellation/rescheduling.

VS-02

3

**C-08**

Prize redemption feature mentioned but no corresponding requirement/use case specified.

Danish Haziq

Add a functional requirement detailing the prize redemption process (conditions, steps, outcomes).

VS-02

4

**C-09**

Authentication method inconsistency: login uses DB check, but interface req�t calls for LDAP SSO.

Danish Haziq

Align the login design with LDAP SSO

VS-02

4

**C\-10**

Some use cases do not include relationships to other relevant use cases, resulting in reduced traceability.

Lee Ken Yu

Review and update the �Relationship to other use cases� field to reflect actual dependencies (such as., link �Track Wellness Progress� to �Set Wellness Goal�).

VS-01

3

**B. Documentation Defect**

**Page No.**

**Validation and Defect Description**

**Detected By**

**Comment/Suggested Fix**

**Session ID**

**Severity (1�5)**

**12**

References not hyperlinked or formatted

Lee Ken Yu

Use IEEE or APA format consistently and ensure all URLs are clickable

VS-01

2

**50-67**

Questionnaire charts lack explanations or interpretations

Ng Jia Hong

Provide short explanations under each chart as to what the responses suggest

VS-02

3

**All**

Inconsistent bullet formatting and spacing

Ng Jia Hong

Standardize bullet styles (symbols, indentation, spacing) using Word�s bullet tool

VS-01

3

**All**

Table formatting inconsistent (spacing, alignment)

Ng Jia Hong

Apply consistent table styling using Table Design features

VS-01

2

**All**

Missing page numbers in header/footer

Lee Ken Yu

Insert page numbers and document versioning on each page

VS-01

3

**All**

Inconsistent table/figure caption naming

Lee Ken Yu

Use the Word's caption format instead of labelling it manually

VS-01

3

**28**

Inconsistent Terminology

Danish Haziq

Use consistent terminology across diagrams (either �Booking� or �Appointment�, based on SRS definition).

VS-01

2

**All**

Inconsistent heading format

Lee Ken Yu

Apply formatting for heading instead type out manually

VS-01

3

**32**

Grammar Error in Display Message

Danish Haziq

Add space and formatting

VS-03

3

**3**

Inconsistent acronym for system: called CWS in scope vs CWP in definitions.

Danish Haziq

Use a single consistent acronym for the system throughout the document.

VS-03

2

�

**C. Agreement Defect**

**Req ID**

**Validation Description/Stakeholder Concern**

**Mismatch**

**Detected By**

**Session ID**

**Severity (1�5)**

**A-01**

Students desired real-time personalized health tips

System provides resources based on previously existing profile, not real-time activity or biometric monitoring (3.1.5 OLD)

Danish Haziq

VS-01

3

**A-02**

Students anticipated consultation notes in health report

System displaying only summary health data; nothing about consultation notes or treatment history (3.1.14 OLD)

Lee Ken Yu

VS-01

3

**A-03**

Staff anticipate consent check prior to seeing wellness report

SRS does not require any form of validation or consent pop-up (3.1.15 OLD)

Ng Jia Hong

VS-01

5

**A-04**

Stakeholders desired in-app notification settings

In-app display of notifications was not explicitly mentioned in SRS, email and Firebase push are emphasized (3.4.5 OLD)

Ng Jia Hong

VS-02

2

**A-05**

Scope mentions supporting student well-being through mental and emotional support.

However, the SRS has no feature fulfilling this (1.3 Product Overview) (3.4.5 OLD)

Danish Haziq

VS-02

3

**A-06**

Omission of online doctor consultation feature.

Identified in stakeholder input but not included in requirements (3.8 Supporting Information). (3.4.5 OLD)

Danish Haziq

VS-02

2

### 3.8.7   Conflict Analysis

**Conflict ID**

**Conflict Description**

**Conflict Analysis**

**Stakeholders Involved**

**Session ID**

**C01**

Fitness staff accessing student health records

Fitness personnel may see/edit health reports, which may reveal sensitive information that is not important to their job. Threat to privacy.

Fitness Staff, Wellness Staff, Privacy Officer

VS-02

**C02**

No student consent mechanism before staff view reports

System gives option to staff to access reports with just Student ID no consent prompt. Inconsistency with PDPA and ethics. 3.1.7.2

Students, Legal Team, Project Manager

VS-02

**C03**

Static health resources vs. dynamic user expectations

Stakeholders requested real-time and behaviour\-based health tips, but system only uses profile preferences.

Students, Health Team

VS-02

**C04**

Booking system lacks waitlist feature

Students were anticipating some option to get on a waitlist when classes/appointments are full, however SRS does not say anything about it, it only says error message. 3.8.1

Students, Admin Staff

VS-02

**C05**

Multiple appointment bookings not explicitly blocked

Unless specifically managed, students could possibly double-book time slots. may create conflicts in schedules. 3.1.2.3

Wellness Staff, Developers

VS-02

**C06**

Lack of backup procedures during third-party API downtime

SRS promises real-time synchronization with medical/fitness systems and does not specify a fallback position. May lead to system crashes.

System Admin, IT Ops Team

VS-02

### 3.8.8   Conflict Resolution

**Conflict ID**

**Conflict Resolution Strategy**

**Resolved (Y/N)**

**Outcome (If Resolved)**

**Justification**

**C01**

Adjusted RBAC so that access could be granted by role; fitness staff may only see fitness-specific numbers. Logs access.

Y

Aligns with privacy roles and prevents unauthorized access. Complies with: 3.7.3 (RBAC for all roles; logs administrative actions), 1.3.4.1 (PDPA-compliant access restrictions), and 1.3.4.5 (user activity logging).

Aligns with privacy roles and prevents unauthorized access.

**C02**

Placed consent request between user and reports; time-stamped.

Y

Supports informed consent and aligns with PDPA. Increases transparency and legal compliance.

Enhances trust and legal compliance.

**C03**

Adapted need to take account of user behavior records and current activity in health resource provision.

Y

Allows tailored delivery of health resources. Enhances personalization and relevance.

Improves relevance and user satisfaction.

**C04**

Added waitlists treatment to booking system auto notify when slots appear.

Y

Users on the waitlist receive real-time notifications and can claim slots immediately.

Prevents lost opportunities and frustration.

**C05**

The issue of double-booking is now also specifically stopped by the additions of a check prior to submission.

Y

Resolves time conflicts and ensures fair access to booking slots.

Resolves time conflicts and ensures fair access.

**C06**

The queuing mechanism and the added data that existed in the form of cache during the downtime in external API. Admins received a notification about the failure of sync.

Y

Improves reliability and ensures users are not affected by external system outages. Builds user trust and ensures data integrity.

Improves reliability and user trust in the platform.

### 3.8.9   Change Log

**Change ID**

**Req ID**

**Summary of Change**

**Proposed By**

**Date**

**Session ID**

  

### 3.8.10                   Requirements Traceability Matrix

**Req ID**

**Requirement Description**

**Linked Goal(s)**

**Feature(s)**

**Use Case(s)**

**Traceability Score (1�4)**

**RQ-01**

Students can book and manage fitness facilities

G1. Improve wellness participation

Facility & Class Booking

Book Fitness Class (3.1.1.4), Manage Fitness Class Schedule (3.1.1.2), Book Facility (3.1.1.3), Manage Facility (3.1.1.1)

4

**RQ-02**

Students and staff manage medical appointments

G2. Enable efficient scheduling

Appointment Management

Manage Appointment (3.1.2.1), Cancel / Reschedule Appointment (3.1.2.2), Book Health Appointment (3.1.2.3)

4

**RQ-03**

Users log in and are granted appropriate access

G6. Ensure secure role-based access

User Access Management

Log In (3.1.3.2), Manage User Accounts and Roles (3.1.3.1)

4

**RQ-04**

Users receive booking reminders and alerts

G5. Improve communication

Notification System

Receive Notification (3.1.4.1)

3

**RQ-05**

Students receive personalized health resources

G3. Personalized wellness guidance

Tailored Health Content

Receive Tailored Health Resources (3.1.5.1)

3

**RQ-06**

Students can set goals and track wellness progress

G4. Wellness progress tracking

Goal Tracking System

Track Wellness Progress (3.1.6.1), Set Wellness Goal (3.1.6.2)

4

**RQ-07**

Students and staff can view and update health reports

G8. Enable health insights and oversight

Health Report Management

View Health Report (3.1.7.1), View Student�s Wellness Report (3.1.7.2), Update Student�s Wellness Report (3.1.7.3)

4

**RQ-08**

Admin monitors system logs and usage data

G7. Improve system maintainability

System Monitoring

Monitor System Usage and Logs (3.1.8.1)

2

### 3.8.11                   Role in Requirements Validation, Negotiation & Management

**Student Name**

**Primary Responsibility**

**No. of Session Participated**

Ng Jia Hong

Lead Validator & Document Editor

3

Lee Ken Yu

Stakeholder Negotiation Lead & Document Editor

3

Danish Haziq

Requirements Analyst &Document Editor

3

### 3.8.12                   Version Control & Configuration Summary

**Commits Made by StudentX:**

**Pull Requests Merged by StudentX:**

**Change Log Entries Made by StudentX:**

4.0     4\. Verification
========================

4.1    4.1 Verification Approach
--------------------------------

●       How:

○       Unit Testing: To verify each function/module works correctly.

○       Functional Testing: To confirm that user actions perform as expected.

○       Integration Testing: To ensure modules work together.

○       Manual User Testing: Development team will simulate end-user behavior to verify overall usability and correctness.  
  

●       Who:

○       Software developers will be responsible for writing and executing unit tests.

○       QA/Test engineers will handle integration, system, and functional testing.

○       Product owners/business analysts will support UAT and validate requirements coverage.

○       IT security specialists will conduct privacy and security verification.

○       Stakeholder Representatives will provide feedback during UAT.

●       When:

○       Unit Testing: Immediately after developing each module.

○       Integration & Functional Testing: Once major components are completed and linked.

○       Final Testing: During the final week before deployment, after all features are integrated.  
  

●       Where:

○       Unit and Integration Testing: Conducted in the developers� and QA team�s test environments.

○       System and Functional Testing: Performed in a dedicated QA/staging environment that stimulates production conditions.

○       UAT: Conducted in a controlled testing environment accessible to stakeholders (on-campus or via secure remote access).

○       Security Testing: Performed within a secure sandbox environment to isolate sensitive data and simulate attacks.

�

4.2    4.2 Verification Criteria
--------------------------------

●       The response time for booking a health appointment should be less than 3 seconds under normal load.

●       The login functionality should successfully authenticate valid users and deny access to unauthorized users.

●       The system should allow students to book fitness classes only if seats are available.

●       The booking system should prevent double-booking of health appointments and facilities.

●       Notifications should be generated and sent to users immediately after booking.

●       Students should be able to view their health reports synced accurately from the university health system.

●       Tailored health resources should be generated based on each student�s wellness goals and activity history.

●       Wellness progress tracking should update immediately after each logged activity or achievement.

●       Students should be able to set their personal wellness goals with measurable targets.

●       Prize redemption should only be available once wellness goals are met.

●       Fitness center staff should be able to manage fitness class schedules through a secure administrative interface.

●       Wellness staff should be able to update and review student health reports without data inconsistency.

●       System administrators should be able to create, assign, and manage user roles and permissions securely.

●       The system should achieve at least 99.5% uptime during active semester weeks.

●       The system should fail gracefully and display meaningful error messages when backend services are unavailable.

●       All data retrieved from external systems (e.g., student database, health center) should match 100% with the source data.

●       Under simulated usage with 10 concurrent users, the system should maintain stable performance with no critical errors.

●       Usability testing should show that at least 90% of users can complete key tasks (e.g., booking or goal tracking) without guidance.

  

�

5.0   5\. Appendices
====================

5.1   5.1 Assumptions and Dependencies
--------------------------------------

Assumptions:

●       The university has an up-to-date and accessible student database that can be used for user authentication and role management.

●       All users (students, fitness center staff, wellness staff and system administrators) have valid and unique credentials provided by the university.

●       The university's health center system and recreation facility management software offer standard APIs or interfaces for integration.

●       Students have regular internet access to use the portal from on- or off-campus locations.

●       The users are familiar with basic digital interfaces and online booking systems.

●       All required regulatory, privacy and data protection standards are clearly defined and enforced.

●       Notifications will be delivered via email.

Dependencies:

●       The system depends on the availability and uptimeup time of the university�s student database for authentication and user role verification.

●       The project is dependent on access to APIs or documentation for the university's health appointment and fitness booking systems.

●       Hosting and deployment depend on the university's IT infrastructure or cloud platform being accessible and sufficient to run the system.

●       Availability of external libraries or tools for calendar management, notification services, and data visualization.

●       Development progress depends on timely feedback from domain stakeholders, including health center staff and recreation center management.

●       Integration with student rewards or incentives systems for prize redemption features, if such a system exists.

●       The system relies on existing campus policies for handling personal wellness data and must integrate within those constraints.

5.2    5.2 Acronyms and Abbreviations
-------------------------------------

1.  **SSO** � Single Sign-On
2.  **SMTP** � Simple Mail Transfer Protocol
3.  **RBAC** � Role-Based Access Control
4.  **HTTPS** � Hypertext Transfer Protocol Secure
5.  **XSS** � Cross-Site Scripting
6.  **AES-256** � Advanced Encryption Standard with 256-bit key
7.  **WCAG** � Web Content Accessibility Guidelines
8.  **UAT** � User Acceptance Testing
9.  **LDAP** � Lightweight Directory Access Protocol
10.  **PDPA** � Personal Data Protection Act
11.  **TLS** � Transport Layer Security
12.  **API** � Application Programming Interface
13.  **REST** � Representational State Transfer
14.  **JSON** � JavaScript Object Notation
15.  **SMTP** � Simple Mail Transfer Protocol
16.  **MySQL** � My Structured Query Language

5.3    5.3 Glossary
-------------------

●       **Admin panel:** A dashboard interface accessible only by administrators for managing users, content and configurations.

●       **Application Programming Interface (API):** A set of rules and endpoints that allow external systems (medical system, fitness center, etc. )etc.) to communicate with the wellness portal.

●       **Appointment slot:** A time window during which students can book consultations with wellness or medical staff.

●       **Booking confirmation:** A notification sent to users after a successful booking.

●       **Class schedule:** Timetable showing the available fitness slots offered by the campus fitness center.

●       **Wellness point:** Reward units earned by students for completing wellness goals, can be used for prize redemption.

●       **Medical report:** A digital record of a student's health history including consultation results available to students and staff.

●       **Personalized resources:** Wellness tips or content tailored based on the student�s and tracked behaviourbehavior.

●       **Prerequisite check:** System mechanism that verifies if a student has met the requirements to perform an action.

●       **Real-time sync:** Immediate data update between systems.

●       **Reschedule:** The act of changing a previously confirmed booking to a different time or date.

●       **Wellness tracker:** A module in the portal that logs and visualizes progress toward wellness goals.

●       **Wellness staff:** Campus personnel responsible for managing health programs and reviewing student progress.

●       **Fitness center staff:** Campus personnel responsible for managing facilities and fitness classes as well as reviewing student progress.

* * *

 [\[D1\]](#_msoanchor_1)Edited the diagram

 [\[D2\]](#_msoanchor_2)Edited the image

 [\[N3\]](#_msoanchor_3)Edited the Post Condition for conflict C07

 [\[N4\]](#_msoanchor_4)Edited the Main Flow for conflict C07

 [\[D5\]](#_msoanchor_5)Edited the image

 [\[N6\]](#_msoanchor_6)Added this paragraph to resolve conflict C08