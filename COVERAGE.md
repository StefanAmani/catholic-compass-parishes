# Catholic Compass parish directory coverage

**STATUS: INCOMPLETE — do not advertise full Tennessee or Wisconsin coverage yet.**

**Audit snapshot (directory version 12, November 7, 2026):** **539** location records (**114 Tennessee**, **425 Wisconsin**). **62** records have a parish website entered; **477** have no website recorded. A nonempty website field does not guarantee the link is current or official.

The current directory combines diocesan source lists and a smaller number of third-party location references. In particular, some Green Bay records came from a Knights of Columbus parish list and still need reconciliation against the Diocese of Green Bay. This snapshot is a count of records, **not a count of verified, active, independent parishes**.

**Active priorities before 1.0:**
1. Reconcile every church site and mission against each diocese's *complete current* directory, and track merged or renamed sites.
2. For each record, independently verify official parish website (as distinct from source directory), street address, and parish identity. Never guess URLs.
3. Prioritize unfinished dioceses of Green Bay, Memphis, and La Crosse; recheck all other dioceses as well.
4. Resolve church-site duplicates/legitimate co-located communities (currently flagged at Stone Lake, WI).
5. Fix app cache freshness so manual checks reliably retrieve the newest directory version.
6. Run browser/mobile tests across representative ZIPs, towns, and all eight dioceses.

**Recent expansion:** Version 10 added 46 La Crosse diocese church locations; version 11 added 22 Green Bay area church references sourced to a third-party list pending diocesan confirmation; version 12 added seven Memphis-area locations grounded in published diocesan references.

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
