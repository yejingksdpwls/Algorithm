### < 문제 설명 > 
다음은 중고 거래 게시판 정보를 담은 USED_GOODS_BOARD 테이블과 중고 거래 게시판 사용자 정보를 담은 USED_GOODS_USER 테이블입니다. USED_GOODS_BOARD 테이블은 다음과 같으며 BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS는 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.
```
    Column_name     Type|           Nullable
    BOARD_ID        VARCHAR(5)	    FALSE
    WRITER_ID    	VARCHAR(50)	    FALSE
    TITLE	        VARCHAR(100)	FALSE
    CONTENTS	    VARCHAR(1000)	FALSE
    PRICE	        NUMBER	        FALSE
    CREATED_DATE	DATE	        FALSE
    STATUS	        VARCHAR(10)	    FALSE
    VIEWS	        NUMBER	        FALSE

```
USED_GOODS_USER 테이블은 다음과 같으며 USER_ID, NICKNAME, CITY, STREET_ADDRESS1, STREET_ADDRESS2, TLNO는 각각 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호를 를 의미합니다.

```
    Column_name	      Type       	 Nullable
    USER_ID	          VARCHAR(50)	 FALSE
    NICKANME	      VARCHAR(100)	 FALSE
    CITY	          VARCHAR(100)	 FALSE
    STREET_ADDRESS1	  VARCHAR(100)	 FALSE
    STREET_ADDRESS2	  VARCHAR(100)	 TRUE
    TLNO	          VARCHAR(20)	 FALSE
```

USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.




### < 처음에 쓴 오답 >
```
SELECT B.USER_ID, B.NICKNAME, SUM(A.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD A INNER JOIN USED_GOODS_USER B ON A.WRITER_ID=B.USER_ID
GROUP BY B.USER_ID
WHERE STATUS='DONE' AND SUM(A.PRICE)>=700000
ORDER BY SUM(A.PRICE)
```

* 오류 원인
	* * STATUS가 'DONE'인 행만 취급 -> WHERE 문에 작성
	* * 'ID별 완료'된 거래 금액의 합계가 70만원 이상 -> GROUP BY 이후 HAVING 문에 작성


### < 정답 >

```
SELECT B.USER_ID, B.NICKNAME, SUM(A.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD A 
INNER JOIN USED_GOODS_USER B ON A.WRITER_ID = B.USER_ID
WHERE STATUS = 'DONE'
GROUP BY B.USER_ID
HAVING SUM(A.PRICE) >= 700000
ORDER BY TOTAL_SALES;
```