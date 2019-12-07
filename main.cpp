/*
    목적 : MySQL 데이터베이스내 존재하는 릴레이션을 C++을 활용해 조회, 출력하는 프로그램
    제작자 : 김재광
    학번 : 2019551008

    Reference
    https://dev.mysql.com/doc/dev/connector-cpp/8.0/
    https://dev.mysql.com/doc/x-devapi-userguide/en/devapi-users-working-with-relational-tables.html
    https://stackoverflow.com/questions/53081091/what-is-the-difference-between-collections-and-tables-in-mysql
    기타 등등
*/

#include <iostream>
// MySQL을 제어하기 위한 헤더파일
#include "mysqlx/xdevapi.h"
using namespace std;
using namespace mysqlx;

// 메뉴를 출력하는 함수
void printMenu();
// 프로그램을 제어하는 함수
void programControl(int user_input);

int main()
{
    int user_input = 0;

    // 프로그램이 동작하는 루프, 2번 입력시 종료됨
    while (user_input != 2)
    {
        printMenu();
        cin >> user_input;

        if (user_input != 1 and user_input != 2)
        {
            cout << "잘못된 명령입니다." << endl;
        }
        else
        {
            programControl(user_input);
        }
    }

    return 0;
}

void printMenu()
{
    cout << "프로그램의 메뉴를 출력합니다." << endl;
    cout << "1. 학교 게시글의 내용을 출력하기" << endl;
    cout << "2. 종료하기" << endl;
    cout << "원하시는 명령을 숫자로 입력하세요." << endl;
}

void programControl(int user_input)
{
    // 1을 입력할시 select구문 동작
    // 2를 입력할시 종료(main에서 구현됨)

    // 유저의 입력 판별
    if (user_input == 1)
    {
        // DB와 연결을 위한 Session객체 생성
        Session session("localhost", 33060, "root", "qwer1234");
        // Session에서 kpu 데이터베이스에 대한 스카마를 schema 객체에 저장
        Schema schema = session.getSchema("kpu", true);
        // schema 객체를 토대로 Table클래스의 객체 생성
        Table bulletin_board = schema.getTable("bulletin_board", true);

        // bulletin_board 테이블을 (select title, conntent)해 RowResult객체인 result에 저장
        RowResult result = bulletin_board.select("title", "content").execute();
        // row들을 전부 추출해 Row클래스형 템플릿 list 함수에 대입
        std::list<Row> rows = result.fetchAll();
        // 결과물 출력
        // rows에서 Row객체 형으로 추출해 출력을 위한 반복
        for (Row row : rows)
        {
            cout << row[0] << endl;
            cout << row[1] << endl
                 << endl;
        }
        // DB 연결세션 종료
        session.close();
    }
    else
    {
        cout << "프로그램을 종료합니다." << endl;
    }
}