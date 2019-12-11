# TABLE DESIGN

## Reader

| <u>RID</u> | password | rName | department | major | borrowNum |
| :-: | :-: | :-: | :-: | :-: | :-: |
| char(20) | char(20) | ntext | nchar(20) | nchar(20) | int |

## Administrator

| AID | PASSWORD |
| :--: | :--: |
| char(15) | char(70) |

## Book

| <u>BID</u> | bName | author | publicationDate | press | sum | currNum |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| char(15) | ntext | ntext | date | nchar(40) | int | int |

## Classify

| <u>CID</u> | <u>classify</u> |
|:-:|:-:|
| char(15) | nchar(20) |

## BorrowRecord

| <u>BID</u> | <u>RID</u> | <u>borrowTime</u> | DEADLINE |
|:-:|:-:|:-:|:-:|
|    int     | char(20) | char(12) | char(12) |

## ReadRecord

| <u>BID</u> | <u>SID</u> | <u>borrowTime</u> | backDate | punish |
|:-:|:-:|:-:|:-:|:-:|
| int | char(20) | char(12) | date | int |

