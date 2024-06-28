public class calc {
    public static void div(int a, int b){
        int result = a/b;
        System.out.println("a / b = " + result);
    }

    public static void sub(int a, int b){
      int result = a-b;
      System.out.println("a - b = " + result);
  }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("첫번째 숫자를 입력해주세요");
        int a = sc.nextInt();

        System.out.println("두번째 숫자를 입력해주세요");
        int b = sc.nextInt();

        System.out.println("수행할 연산 기호를 입력해주세요(+, -, *, /, 종료)");
        String act = sc.next();

        switch(act){
            case "종료":
                break;
            case "+":
                add(a,b);
                break;
            case "-":
                sub(a,b);
                break;
            case "*":
                mul(a,b);
                break;
            case "/":
                div(a,b);
                break;
        }
    }
}

