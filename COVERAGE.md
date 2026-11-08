# Catholic Compass parish directory coverage

**STATUS: INCOMPLETE — Do not advertise full Tennessee or Wisconsin coverage yet.**

**Audit baseline (directory version 9, November 7, 2026):** 464 location records (107 Tennessee, 357 Wisconsin). Only 29 records have a nonempty parish website; 435 need website matching/verification. A listed URL may itself be outdated. These numbers count locations, not unique parish organizations.

**Records currently attributed to official diocesan source pages:**

| State | Diocese | Directory records |
|---|---|---:|
| Tennessee | Nashville | 41 |
| Tennessee | Knoxville | 50 |
| Tennessee | Memphis | 16 |
| Wisconsin | Milwaukee | 166 |
| Wisconsin | Madison | 69 |
| Wisconsin | Green Bay | 12 |
| Wisconsin | La Crosse | 31 |
| Wisconsin | Superior | 79 |

**Priority gaps:** Green Bay, La Crosse, and Memphis have especially small samples. Every diocese still needs an official source-to-record reconciliation. The current Green Bay sample came from a Hispanic ministry document, **not** a complete parish directory. Some names or websites may have changed due to mergers.

## Official source checklist

- [ ] Tennessee — Diocese of Nashville: https://dioceseofnashville.com/find-a-church/
- [ ] Tennessee — Diocese of Knoxville: https://www.dioknox.org/parishes
- [ ] Tennessee — Diocese of Memphis: https://cdom.org/our-church/
- [ ] Wisconsin — Archdiocese of Milwaukee: https://www.archmil.org/maps/parishes
- [ ] Wisconsin — Diocese of Madison: https://www.madisondiocese.org/directory
- [ ] Wisconsin — Diocese of Green Bay: https://www.gbdioc.org/worship-jesus/find-a-parish/
- [ ] Wisconsin — Diocese of La Crosse: https://diolc.org/parishes/
- [ ] Wisconsin — Diocese of Superior: https://catholicdos.org/parishfinder

## Release acceptance criteria

1. Reconcile records against every source, including rural communities, parish missions and multi-campus parishes.
2. Track each church's physical address and distinguish official parish websites from other directories.
3. Record merged or renamed parishes without misleading duplicates.
4. Verify state, city and ZIP search behavior against sample cities in all eight dioceses.
5. Review rights and access policies before any automated bulk collection; respect usage restrictions.
6. Confirm automatic app refresh and offline cache retain the last valid directory on error.
7. Check 60-day link reports manually; link reachability checks are not closure/merger verification.

The GitHub workflow is a bi-monthly **link check**, not a guarantee of data currency or statewide completeness.
