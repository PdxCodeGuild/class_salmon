const wordNumberDict = {
0: "zero",
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eightteen",
19: "nineteen",
20: "twenty",
21: "twenty one",
22: "twenty two",
23: "twenty three",
24: "twenty four",
25: "twenty five",
26: "twenty six",
27: "twenty seven",
28: "twenty eight",
29: "twenty nine",
30: "thirty",
31: "thirty one",
32: "thirty two",
33: "thirty three",
34: "thirty four",
35: "thirty five",
36: "thirty six",
37: "thirty seven",
38: "thirty eight",
39: "thirty nine",
40: "fourty",
41: "fourty one",
42: "fourty two",
43: "fourty three",
44: "fourty four",
45: "fourty five",
46: "fourty six",
47: "fourty seven",
48: "fourty eight",
49: "fourty nine",
50: "fifty",
51: "fifty one",
52: "fifty two",
53: "fifty three",
54: "fifty four",
55: "fifty five",
56: "fifty six",
57: "fifty seven",
58: "fifty eight",
59: "fifty nine",
60: "sixty",
61: "sixty one",
62: "sixty two",
63: "sixty three",
64: "sixty four",
65: "sixty five",
66: "sixty six",
67: "sixty seven",
68: "sixty eight",
69: "sixty nine",
70: "seventy",
71: "seventy one",
72: "seventy two",
73: "seventy three",
74: "seventy four",
75: "seventy five",
76: "seventy six",
77: "seventy seven",
78: "seventy eight",
79: "seventy nine",
80: "eighty",
81: "eighty one",
82: "eighty two",
83: "eighty three",
84: "eighty four",
85: "eighty five",
86: "eighty six",
87: "eighty seven",
88: "eighty eight",
89: "eighty nine",
90: "ninety",
91: "ninety one",
92: "ninety two",
93: "ninety three",
94: "ninety four",
95: "ninety five",
96: "ninety six",
97: "ninety seven",
98: "ninety eight",
99: "ninety nine",
100: "one hundred",
101: "one hundred and one",
102: "one hundred and two",
103: "one hundred and three",
104: "one hundred and four",
105: "one hundred and five",
106: "one hundred and six",
107: "one hundred and seven",
108: "one hundred and eight",
109: "one hundred and nine",
110: "one hundred and ten",
111: "one hundred and eleven",
112: "one hundred and twelve",
113: "one hundred and thirteen",
114: "one hundred and fourteen",
115: "one hundred and fifteen",
116: "one hundred and sixteen",
117: "one hundred and seventeen",
118: "one hundred and eightteen",
119: "one hundred and nineteen",
120: "one hundred and twenty",
121: "one hundred and twenty one",
122: "one hundred and twenty two",
123: "one hundred and twenty three",
124: "one hundred and twenty four",
125: "one hundred and twenty five",
126: "one hundred and twenty six",
127: "one hundred and twenty seven",
128: "one hundred and twenty eight",
129: "one hundred and twenty nine",
130: "one hundred and thirty",
131: "one hundred and thirty one",
132: "one hundred and thirty two",
133: "one hundred and thirty three",
134: "one hundred and thirty four",
135: "one hundred and thirty five",
136: "one hundred and thirty six",
137: "one hundred and thirty seven",
138: "one hundred and thirty eight",
139: "one hundred and thirty nine",
140: "one hundred and fourty",
141: "one hundred and fourty one",
142: "one hundred and fourty two",
143: "one hundred and fourty three",
144: "one hundred and fourty four",
145: "one hundred and fourty five",
146: "one hundred and fourty six",
147: "one hundred and fourty seven",
148: "one hundred and fourty eight",
149: "one hundred and fourty nine",
150: "one hundred and fifty",
151: "one hundred and fifty one",
152: "one hundred and fifty two",
153: "one hundred and fifty three",
154: "one hundred and fifty four",
155: "one hundred and fifty five",
156: "one hundred and fifty six",
157: "one hundred and fifty seven",
158: "one hundred and fifty eight",
159: "one hundred and fifty nine",
160: "one hundred and sixty",
161: "one hundred and sixty one",
162: "one hundred and sixty two",
163: "one hundred and sixty three",
164: "one hundred and sixty four",
165: "one hundred and sixty five",
166: "one hundred and sixty six",
167: "one hundred and sixty seven",
168: "one hundred and sixty eight",
169: "one hundred and sixty nine",
170: "one hundred and seventy",
171: "one hundred and seventy one",
172: "one hundred and seventy two",
173: "one hundred and seventy three",
174: "one hundred and seventy four",
175: "one hundred and seventy five",
176: "one hundred and seventy six",
177: "one hundred and seventy seven",
178: "one hundred and seventy eight",
179: "one hundred and seventy nine",
180: "one hundred and eighty",
181: "one hundred and eighty one",
182: "one hundred and eighty two",
183: "one hundred and eighty three",
184: "one hundred and eighty four",
185: "one hundred and eighty five",
186: "one hundred and eighty six",
187: "one hundred and eighty seven",
188: "one hundred and eighty eight",
189: "one hundred and eighty nine",
190: "one hundred and ninety",
191: "one hundred and ninety one",
192: "one hundred and ninety two",
193: "one hundred and ninety three",
194: "one hundred and ninety four",
195: "one hundred and ninety five",
196: "one hundred and ninety six",
197: "one hundred and ninety seven",
198: "one hundred and ninety eight",
199: "one hundred and ninety nine",
200: "two hundred",
201: "two hundred and one",
202: "two hundred and two",
203: "two hundred and three",
204: "two hundred and four",
205: "two hundred and five",
206: "two hundred and six",
207: "two hundred and seven",
208: "two hundred and eight",
209: "two hundred and nine",
210: "two hundred and ten",
211: "two hundred and eleven",
212: "two hundred and twelve",
213: "two hundred and thirteen",
214: "two hundred and fourteen",
215: "two hundred and fifteen",
216: "two hundred and sixteen",
217: "two hundred and seventeen",
218: "two hundred and eightteen",
219: "two hundred and nineteen",
220: "two hundred and twenty",
221: "two hundred and twenty one",
222: "two hundred and twenty two",
223: "two hundred and twenty three",
224: "two hundred and twenty four",
225: "two hundred and twenty five",
226: "two hundred and twenty six",
227: "two hundred and twenty seven",
228: "two hundred and twenty eight",
229: "two hundred and twenty nine",
230: "two hundred and thirty",
231: "two hundred and thirty one",
232: "two hundred and thirty two",
233: "two hundred and thirty three",
234: "two hundred and thirty four",
235: "two hundred and thirty five",
236: "two hundred and thirty six",
237: "two hundred and thirty seven",
238: "two hundred and thirty eight",
239: "two hundred and thirty nine",
240: "two hundred and fourty",
241: "two hundred and fourty one",
242: "two hundred and fourty two",
243: "two hundred and fourty three",
244: "two hundred and fourty four",
245: "two hundred and fourty five",
246: "two hundred and fourty six",
247: "two hundred and fourty seven",
248: "two hundred and fourty eight",
249: "two hundred and fourty nine",
250: "two hundred and fifty",
251: "two hundred and fifty one",
252: "two hundred and fifty two",
253: "two hundred and fifty three",
254: "two hundred and fifty four",
255: "two hundred and fifty five",
256: "two hundred and fifty six",
257: "two hundred and fifty seven",
258: "two hundred and fifty eight",
259: "two hundred and fifty nine",
260: "two hundred and sixty",
261: "two hundred and sixty one",
262: "two hundred and sixty two",
263: "two hundred and sixty three",
264: "two hundred and sixty four",
265: "two hundred and sixty five",
266: "two hundred and sixty six",
267: "two hundred and sixty seven",
268: "two hundred and sixty eight",
269: "two hundred and sixty nine",
270: "two hundred and seventy",
271: "two hundred and seventy one",
272: "two hundred and seventy two",
273: "two hundred and seventy three",
274: "two hundred and seventy four",
275: "two hundred and seventy five",
276: "two hundred and seventy six",
277: "two hundred and seventy seven",
278: "two hundred and seventy eight",
279: "two hundred and seventy nine",
280: "two hundred and eighty",
281: "two hundred and eighty one",
282: "two hundred and eighty two",
283: "two hundred and eighty three",
284: "two hundred and eighty four",
285: "two hundred and eighty five",
286: "two hundred and eighty six",
287: "two hundred and eighty seven",
288: "two hundred and eighty eight",
289: "two hundred and eighty nine",
290: "two hundred and ninety",
291: "two hundred and ninety one",
292: "two hundred and ninety two",
293: "two hundred and ninety three",
294: "two hundred and ninety four",
295: "two hundred and ninety five",
296: "two hundred and ninety six",
297: "two hundred and ninety seven",
298: "two hundred and ninety eight",
299: "two hundred and ninety nine",
300: "three hundred",
301: "three hundred and one",
302: "three hundred and two",
303: "three hundred and three",
304: "three hundred and four",
305: "three hundred and five",
306: "three hundred and six",
307: "three hundred and seven",
308: "three hundred and eight",
309: "three hundred and nine",
310: "three hundred and ten",
311: "three hundred and eleven",
312: "three hundred and twelve",
313: "three hundred and thirteen",
314: "three hundred and fourteen",
315: "three hundred and fifteen",
316: "three hundred and sixteen",
317: "three hundred and seventeen",
318: "three hundred and eightteen",
319: "three hundred and nineteen",
320: "three hundred and twenty",
321: "three hundred and twenty one",
322: "three hundred and twenty two",
323: "three hundred and twenty three",
324: "three hundred and twenty four",
325: "three hundred and twenty five",
326: "three hundred and twenty six",
327: "three hundred and twenty seven",
328: "three hundred and twenty eight",
329: "three hundred and twenty nine",
330: "three hundred and thirty",
331: "three hundred and thirty one",
332: "three hundred and thirty two",
333: "three hundred and thirty three",
334: "three hundred and thirty four",
335: "three hundred and thirty five",
336: "three hundred and thirty six",
337: "three hundred and thirty seven",
338: "three hundred and thirty eight",
339: "three hundred and thirty nine",
340: "three hundred and fourty",
341: "three hundred and fourty one",
342: "three hundred and fourty two",
343: "three hundred and fourty three",
344: "three hundred and fourty four",
345: "three hundred and fourty five",
346: "three hundred and fourty six",
347: "three hundred and fourty seven",
348: "three hundred and fourty eight",
349: "three hundred and fourty nine",
350: "three hundred and fifty",
351: "three hundred and fifty one",
352: "three hundred and fifty two",
353: "three hundred and fifty three",
354: "three hundred and fifty four",
355: "three hundred and fifty five",
356: "three hundred and fifty six",
357: "three hundred and fifty seven",
358: "three hundred and fifty eight",
359: "three hundred and fifty nine",
360: "three hundred and sixty",
361: "three hundred and sixty one",
362: "three hundred and sixty two",
363: "three hundred and sixty three",
364: "three hundred and sixty four",
365: "three hundred and sixty five",
366: "three hundred and sixty six",
367: "three hundred and sixty seven",
368: "three hundred and sixty eight",
369: "three hundred and sixty nine",
370: "three hundred and seventy",
371: "three hundred and seventy one",
372: "three hundred and seventy two",
373: "three hundred and seventy three",
374: "three hundred and seventy four",
375: "three hundred and seventy five",
376: "three hundred and seventy six",
377: "three hundred and seventy seven",
378: "three hundred and seventy eight",
379: "three hundred and seventy nine",
380: "three hundred and eighty",
381: "three hundred and eighty one",
382: "three hundred and eighty two",
383: "three hundred and eighty three",
384: "three hundred and eighty four",
385: "three hundred and eighty five",
386: "three hundred and eighty six",
387: "three hundred and eighty seven",
388: "three hundred and eighty eight",
389: "three hundred and eighty nine",
390: "three hundred and ninety",
391: "three hundred and ninety one",
392: "three hundred and ninety two",
393: "three hundred and ninety three",
394: "three hundred and ninety four",
395: "three hundred and ninety five",
396: "three hundred and ninety six",
397: "three hundred and ninety seven",
398: "three hundred and ninety eight",
399: "three hundred and ninety nine",
400: "four hundred",
401: "four hundred and one",
402: "four hundred and two",
403: "four hundred and three",
404: "four hundred and four",
405: "four hundred and five",
406: "four hundred and six",
407: "four hundred and seven",
408: "four hundred and eight",
409: "four hundred and nine",
410: "four hundred and ten",
411: "four hundred and eleven",
412: "four hundred and twelve",
413: "four hundred and thirteen",
414: "four hundred and fourteen",
415: "four hundred and fifteen",
416: "four hundred and sixteen",
417: "four hundred and seventeen",
418: "four hundred and eightteen",
419: "four hundred and nineteen",
420: "four hundred and twenty",
421: "four hundred and twenty one",
422: "four hundred and twenty two",
423: "four hundred and twenty three",
424: "four hundred and twenty four",
425: "four hundred and twenty five",
426: "four hundred and twenty six",
427: "four hundred and twenty seven",
428: "four hundred and twenty eight",
429: "four hundred and twenty nine",
430: "four hundred and thirty",
431: "four hundred and thirty one",
432: "four hundred and thirty two",
433: "four hundred and thirty three",
434: "four hundred and thirty four",
435: "four hundred and thirty five",
436: "four hundred and thirty six",
437: "four hundred and thirty seven",
438: "four hundred and thirty eight",
439: "four hundred and thirty nine",
440: "four hundred and fourty",
441: "four hundred and fourty one",
442: "four hundred and fourty two",
443: "four hundred and fourty three",
444: "four hundred and fourty four",
445: "four hundred and fourty five",
446: "four hundred and fourty six",
447: "four hundred and fourty seven",
448: "four hundred and fourty eight",
449: "four hundred and fourty nine",
450: "four hundred and fifty",
451: "four hundred and fifty one",
452: "four hundred and fifty two",
453: "four hundred and fifty three",
454: "four hundred and fifty four",
455: "four hundred and fifty five",
456: "four hundred and fifty six",
457: "four hundred and fifty seven",
458: "four hundred and fifty eight",
459: "four hundred and fifty nine",
460: "four hundred and sixty",
461: "four hundred and sixty one",
462: "four hundred and sixty two",
463: "four hundred and sixty three",
464: "four hundred and sixty four",
465: "four hundred and sixty five",
466: "four hundred and sixty six",
467: "four hundred and sixty seven",
468: "four hundred and sixty eight",
469: "four hundred and sixty nine",
470: "four hundred and seventy",
471: "four hundred and seventy one",
472: "four hundred and seventy two",
473: "four hundred and seventy three",
474: "four hundred and seventy four",
475: "four hundred and seventy five",
476: "four hundred and seventy six",
477: "four hundred and seventy seven",
478: "four hundred and seventy eight",
479: "four hundred and seventy nine",
480: "four hundred and eighty",
481: "four hundred and eighty one",
482: "four hundred and eighty two",
483: "four hundred and eighty three",
484: "four hundred and eighty four",
485: "four hundred and eighty five",
486: "four hundred and eighty six",
487: "four hundred and eighty seven",
488: "four hundred and eighty eight",
489: "four hundred and eighty nine",
490: "four hundred and ninety",
491: "four hundred and ninety one",
492: "four hundred and ninety two",
493: "four hundred and ninety three",
494: "four hundred and ninety four",
495: "four hundred and ninety five",
496: "four hundred and ninety six",
497: "four hundred and ninety seven",
498: "four hundred and ninety eight",
499: "four hundred and ninety nine",
500: "five hundred",
501: "five hundred and one",
502: "five hundred and two",
503: "five hundred and three",
504: "five hundred and four",
505: "five hundred and five",
506: "five hundred and six",
507: "five hundred and seven",
508: "five hundred and eight",
509: "five hundred and nine",
510: "five hundred and ten",
511: "five hundred and eleven",
512: "five hundred and twelve",
513: "five hundred and thirteen",
514: "five hundred and fourteen",
515: "five hundred and fifteen",
516: "five hundred and sixteen",
517: "five hundred and seventeen",
518: "five hundred and eightteen",
519: "five hundred and nineteen",
520: "five hundred and twenty",
521: "five hundred and twenty one",
522: "five hundred and twenty two",
523: "five hundred and twenty three",
524: "five hundred and twenty four",
525: "five hundred and twenty five",
526: "five hundred and twenty six",
527: "five hundred and twenty seven",
528: "five hundred and twenty eight",
529: "five hundred and twenty nine",
530: "five hundred and thirty",
531: "five hundred and thirty one",
532: "five hundred and thirty two",
533: "five hundred and thirty three",
534: "five hundred and thirty four",
535: "five hundred and thirty five",
536: "five hundred and thirty six",
537: "five hundred and thirty seven",
538: "five hundred and thirty eight",
539: "five hundred and thirty nine",
540: "five hundred and fourty",
541: "five hundred and fourty one",
542: "five hundred and fourty two",
543: "five hundred and fourty three",
544: "five hundred and fourty four",
545: "five hundred and fourty five",
546: "five hundred and fourty six",
547: "five hundred and fourty seven",
548: "five hundred and fourty eight",
549: "five hundred and fourty nine",
550: "five hundred and fifty",
551: "five hundred and fifty one",
552: "five hundred and fifty two",
553: "five hundred and fifty three",
554: "five hundred and fifty four",
555: "five hundred and fifty five",
556: "five hundred and fifty six",
557: "five hundred and fifty seven",
558: "five hundred and fifty eight",
559: "five hundred and fifty nine",
560: "five hundred and sixty",
561: "five hundred and sixty one",
562: "five hundred and sixty two",
563: "five hundred and sixty three",
564: "five hundred and sixty four",
565: "five hundred and sixty five",
566: "five hundred and sixty six",
567: "five hundred and sixty seven",
568: "five hundred and sixty eight",
569: "five hundred and sixty nine",
570: "five hundred and seventy",
571: "five hundred and seventy one",
572: "five hundred and seventy two",
573: "five hundred and seventy three",
574: "five hundred and seventy four",
575: "five hundred and seventy five",
576: "five hundred and seventy six",
577: "five hundred and seventy seven",
578: "five hundred and seventy eight",
579: "five hundred and seventy nine",
580: "five hundred and eighty",
581: "five hundred and eighty one",
582: "five hundred and eighty two",
583: "five hundred and eighty three",
584: "five hundred and eighty four",
585: "five hundred and eighty five",
586: "five hundred and eighty six",
587: "five hundred and eighty seven",
588: "five hundred and eighty eight",
589: "five hundred and eighty nine",
590: "five hundred and ninety",
591: "five hundred and ninety one",
592: "five hundred and ninety two",
593: "five hundred and ninety three",
594: "five hundred and ninety four",
595: "five hundred and ninety five",
596: "five hundred and ninety six",
597: "five hundred and ninety seven",
598: "five hundred and ninety eight",
599: "five hundred and ninety nine",
600: "six hundred",
601: "six hundred and one",
602: "six hundred and two",
603: "six hundred and three",
604: "six hundred and four",
605: "six hundred and five",
606: "six hundred and six",
607: "six hundred and seven",
608: "six hundred and eight",
609: "six hundred and nine",
610: "six hundred and ten",
611: "six hundred and eleven",
612: "six hundred and twelve",
613: "six hundred and thirteen",
614: "six hundred and fourteen",
615: "six hundred and fifteen",
616: "six hundred and sixteen",
617: "six hundred and seventeen",
618: "six hundred and eightteen",
619: "six hundred and nineteen",
620: "six hundred and twenty",
621: "six hundred and twenty one",
622: "six hundred and twenty two",
623: "six hundred and twenty three",
624: "six hundred and twenty four",
625: "six hundred and twenty five",
626: "six hundred and twenty six",
627: "six hundred and twenty seven",
628: "six hundred and twenty eight",
629: "six hundred and twenty nine",
630: "six hundred and thirty",
631: "six hundred and thirty one",
632: "six hundred and thirty two",
633: "six hundred and thirty three",
634: "six hundred and thirty four",
635: "six hundred and thirty five",
636: "six hundred and thirty six",
637: "six hundred and thirty seven",
638: "six hundred and thirty eight",
639: "six hundred and thirty nine",
640: "six hundred and fourty",
641: "six hundred and fourty one",
642: "six hundred and fourty two",
643: "six hundred and fourty three",
644: "six hundred and fourty four",
645: "six hundred and fourty five",
646: "six hundred and fourty six",
647: "six hundred and fourty seven",
648: "six hundred and fourty eight",
649: "six hundred and fourty nine",
650: "six hundred and fifty",
651: "six hundred and fifty one",
652: "six hundred and fifty two",
653: "six hundred and fifty three",
654: "six hundred and fifty four",
655: "six hundred and fifty five",
656: "six hundred and fifty six",
657: "six hundred and fifty seven",
658: "six hundred and fifty eight",
659: "six hundred and fifty nine",
660: "six hundred and sixty",
661: "six hundred and sixty one",
662: "six hundred and sixty two",
663: "six hundred and sixty three",
664: "six hundred and sixty four",
665: "six hundred and sixty five",
666: "six hundred and sixty six",
667: "six hundred and sixty seven",
668: "six hundred and sixty eight",
669: "six hundred and sixty nine",
670: "six hundred and seventy",
671: "six hundred and seventy one",
672: "six hundred and seventy two",
673: "six hundred and seventy three",
674: "six hundred and seventy four",
675: "six hundred and seventy five",
676: "six hundred and seventy six",
677: "six hundred and seventy seven",
678: "six hundred and seventy eight",
679: "six hundred and seventy nine",
680: "six hundred and eighty",
681: "six hundred and eighty one",
682: "six hundred and eighty two",
683: "six hundred and eighty three",
684: "six hundred and eighty four",
685: "six hundred and eighty five",
686: "six hundred and eighty six",
687: "six hundred and eighty seven",
688: "six hundred and eighty eight",
689: "six hundred and eighty nine",
690: "six hundred and ninety",
691: "six hundred and ninety one",
692: "six hundred and ninety two",
693: "six hundred and ninety three",
694: "six hundred and ninety four",
695: "six hundred and ninety five",
696: "six hundred and ninety six",
697: "six hundred and ninety seven",
698: "six hundred and ninety eight",
699: "six hundred and ninety nine",
700: "seven hundred",
701: "seven hundred and one",
702: "seven hundred and two",
703: "seven hundred and three",
704: "seven hundred and four",
705: "seven hundred and five",
706: "seven hundred and six",
707: "seven hundred and seven",
708: "seven hundred and eight",
709: "seven hundred and nine",
710: "seven hundred and ten",
711: "seven hundred and eleven",
712: "seven hundred and twelve",
713: "seven hundred and thirteen",
714: "seven hundred and fourteen",
715: "seven hundred and fifteen",
716: "seven hundred and sixteen",
717: "seven hundred and seventeen",
718: "seven hundred and eightteen",
719: "seven hundred and nineteen",
720: "seven hundred and twenty",
721: "seven hundred and twenty one",
722: "seven hundred and twenty two",
723: "seven hundred and twenty three",
724: "seven hundred and twenty four",
725: "seven hundred and twenty five",
726: "seven hundred and twenty six",
727: "seven hundred and twenty seven",
728: "seven hundred and twenty eight",
729: "seven hundred and twenty nine",
730: "seven hundred and thirty",
731: "seven hundred and thirty one",
732: "seven hundred and thirty two",
733: "seven hundred and thirty three",
734: "seven hundred and thirty four",
735: "seven hundred and thirty five",
736: "seven hundred and thirty six",
737: "seven hundred and thirty seven",
738: "seven hundred and thirty eight",
739: "seven hundred and thirty nine",
740: "seven hundred and fourty",
741: "seven hundred and fourty one",
742: "seven hundred and fourty two",
743: "seven hundred and fourty three",
744: "seven hundred and fourty four",
745: "seven hundred and fourty five",
746: "seven hundred and fourty six",
747: "seven hundred and fourty seven",
748: "seven hundred and fourty eight",
749: "seven hundred and fourty nine",
750: "seven hundred and fifty",
751: "seven hundred and fifty one",
752: "seven hundred and fifty two",
753: "seven hundred and fifty three",
754: "seven hundred and fifty four",
755: "seven hundred and fifty five",
756: "seven hundred and fifty six",
757: "seven hundred and fifty seven",
758: "seven hundred and fifty eight",
759: "seven hundred and fifty nine",
760: "seven hundred and sixty",
761: "seven hundred and sixty one",
762: "seven hundred and sixty two",
763: "seven hundred and sixty three",
764: "seven hundred and sixty four",
765: "seven hundred and sixty five",
766: "seven hundred and sixty six",
767: "seven hundred and sixty seven",
768: "seven hundred and sixty eight",
769: "seven hundred and sixty nine",
770: "seven hundred and seventy",
771: "seven hundred and seventy one",
772: "seven hundred and seventy two",
773: "seven hundred and seventy three",
774: "seven hundred and seventy four",
775: "seven hundred and seventy five",
776: "seven hundred and seventy six",
777: "seven hundred and seventy seven",
778: "seven hundred and seventy eight",
779: "seven hundred and seventy nine",
780: "seven hundred and eighty",
781: "seven hundred and eighty one",
782: "seven hundred and eighty two",
783: "seven hundred and eighty three",
784: "seven hundred and eighty four",
785: "seven hundred and eighty five",
786: "seven hundred and eighty six",
787: "seven hundred and eighty seven",
788: "seven hundred and eighty eight",
789: "seven hundred and eighty nine",
790: "seven hundred and ninety",
791: "seven hundred and ninety one",
792: "seven hundred and ninety two",
793: "seven hundred and ninety three",
794: "seven hundred and ninety four",
795: "seven hundred and ninety five",
796: "seven hundred and ninety six",
797: "seven hundred and ninety seven",
798: "seven hundred and ninety eight",
799: "seven hundred and ninety nine",
800: "eight hundred",
801: "eight hundred and one",
802: "eight hundred and two",
803: "eight hundred and three",
804: "eight hundred and four",
805: "eight hundred and five",
806: "eight hundred and six",
807: "eight hundred and seven",
808: "eight hundred and eight",
809: "eight hundred and nine",
810: "eight hundred and ten",
811: "eight hundred and eleven",
812: "eight hundred and twelve",
813: "eight hundred and thirteen",
814: "eight hundred and fourteen",
815: "eight hundred and fifteen",
816: "eight hundred and sixteen",
817: "eight hundred and seventeen",
818: "eight hundred and eightteen",
819: "eight hundred and nineteen",
820: "eight hundred and twenty",
821: "eight hundred and twenty one",
822: "eight hundred and twenty two",
823: "eight hundred and twenty three",
824: "eight hundred and twenty four",
825: "eight hundred and twenty five",
826: "eight hundred and twenty six",
827: "eight hundred and twenty seven",
828: "eight hundred and twenty eight",
829: "eight hundred and twenty nine",
830: "eight hundred and thirty",
831: "eight hundred and thirty one",
832: "eight hundred and thirty two",
833: "eight hundred and thirty three",
834: "eight hundred and thirty four",
835: "eight hundred and thirty five",
836: "eight hundred and thirty six",
837: "eight hundred and thirty seven",
838: "eight hundred and thirty eight",
839: "eight hundred and thirty nine",
840: "eight hundred and fourty",
841: "eight hundred and fourty one",
842: "eight hundred and fourty two",
843: "eight hundred and fourty three",
844: "eight hundred and fourty four",
845: "eight hundred and fourty five",
846: "eight hundred and fourty six",
847: "eight hundred and fourty seven",
848: "eight hundred and fourty eight",
849: "eight hundred and fourty nine",
850: "eight hundred and fifty",
851: "eight hundred and fifty one",
852: "eight hundred and fifty two",
853: "eight hundred and fifty three",
854: "eight hundred and fifty four",
855: "eight hundred and fifty five",
856: "eight hundred and fifty six",
857: "eight hundred and fifty seven",
858: "eight hundred and fifty eight",
859: "eight hundred and fifty nine",
860: "eight hundred and sixty",
861: "eight hundred and sixty one",
862: "eight hundred and sixty two",
863: "eight hundred and sixty three",
864: "eight hundred and sixty four",
865: "eight hundred and sixty five",
866: "eight hundred and sixty six",
867: "eight hundred and sixty seven",
868: "eight hundred and sixty eight",
869: "eight hundred and sixty nine",
870: "eight hundred and seventy",
871: "eight hundred and seventy one",
872: "eight hundred and seventy two",
873: "eight hundred and seventy three",
874: "eight hundred and seventy four",
875: "eight hundred and seventy five",
876: "eight hundred and seventy six",
877: "eight hundred and seventy seven",
878: "eight hundred and seventy eight",
879: "eight hundred and seventy nine",
880: "eight hundred and eighty",
881: "eight hundred and eighty one",
882: "eight hundred and eighty two",
883: "eight hundred and eighty three",
884: "eight hundred and eighty four",
885: "eight hundred and eighty five",
886: "eight hundred and eighty six",
887: "eight hundred and eighty seven",
888: "eight hundred and eighty eight",
889: "eight hundred and eighty nine",
890: "eight hundred and ninety",
891: "eight hundred and ninety one",
892: "eight hundred and ninety two",
893: "eight hundred and ninety three",
894: "eight hundred and ninety four",
895: "eight hundred and ninety five",
896: "eight hundred and ninety six",
897: "eight hundred and ninety seven",
898: "eight hundred and ninety eight",
899: "eight hundred and ninety nine",
900: "nine hundred",
901: "nine hundred and one",
902: "nine hundred and two",
903: "nine hundred and three",
904: "nine hundred and four",
905: "nine hundred and five",
906: "nine hundred and six",
907: "nine hundred and seven",
908: "nine hundred and eight",
909: "nine hundred and nine",
910: "nine hundred and ten",
911: "nine hundred and eleven",
912: "nine hundred and twelve",
913: "nine hundred and thirteen",
914: "nine hundred and fourteen",
915: "nine hundred and fifteen",
916: "nine hundred and sixteen",
917: "nine hundred and seventeen",
918: "nine hundred and eightteen",
919: "nine hundred and nineteen",
920: "nine hundred and twenty",
921: "nine hundred and twenty one",
922: "nine hundred and twenty two",
923: "nine hundred and twenty three",
924: "nine hundred and twenty four",
925: "nine hundred and twenty five",
926: "nine hundred and twenty six",
927: "nine hundred and twenty seven",
928: "nine hundred and twenty eight",
929: "nine hundred and twenty nine",
930: "nine hundred and thirty",
931: "nine hundred and thirty one",
932: "nine hundred and thirty two",
933: "nine hundred and thirty three",
934: "nine hundred and thirty four",
935: "nine hundred and thirty five",
936: "nine hundred and thirty six",
937: "nine hundred and thirty seven",
938: "nine hundred and thirty eight",
939: "nine hundred and thirty nine",
940: "nine hundred and fourty",
941: "nine hundred and fourty one",
942: "nine hundred and fourty two",
943: "nine hundred and fourty three",
944: "nine hundred and fourty four",
945: "nine hundred and fourty five",
946: "nine hundred and fourty six",
947: "nine hundred and fourty seven",
948: "nine hundred and fourty eight",
949: "nine hundred and fourty nine",
950: "nine hundred and fifty",
951: "nine hundred and fifty one",
952: "nine hundred and fifty two",
953: "nine hundred and fifty three",
954: "nine hundred and fifty four",
955: "nine hundred and fifty five",
956: "nine hundred and fifty six",
957: "nine hundred and fifty seven",
958: "nine hundred and fifty eight",
959: "nine hundred and fifty nine",
960: "nine hundred and sixty",
961: "nine hundred and sixty one",
962: "nine hundred and sixty two",
963: "nine hundred and sixty three",
964: "nine hundred and sixty four",
965: "nine hundred and sixty five",
966: "nine hundred and sixty six",
967: "nine hundred and sixty seven",
968: "nine hundred and sixty eight",
969: "nine hundred and sixty nine",
970: "nine hundred and seventy",
971: "nine hundred and seventy one",
972: "nine hundred and seventy two",
973: "nine hundred and seventy three",
974: "nine hundred and seventy four",
975: "nine hundred and seventy five",
976: "nine hundred and seventy six",
977: "nine hundred and seventy seven",
978: "nine hundred and seventy eight",
979: "nine hundred and seventy nine",
980: "nine hundred and eighty",
981: "nine hundred and eighty one",
982: "nine hundred and eighty two",
983: "nine hundred and eighty three",
984: "nine hundred and eighty four",
985: "nine hundred and eighty five",
986: "nine hundred and eighty six",
987: "nine hundred and eighty seven",
988: "nine hundred and eighty eight",
989: "nine hundred and eighty nine",
990: "nine hundred and ninety",
991: "nine hundred and ninety one",
992: "nine hundred and ninety two",
993: "nine hundred and ninety three",
994: "nine hundred and ninety four",
995: "nine hundred and ninety five",
996: "nine hundred and ninety six",
997: "nine hundred and ninety seven",
998: "nine hundred and ninety eight",
999: "nine hundred and ninety nine",
}

alert(wordNumberDict[prompt("Enter a number between 0-999")])