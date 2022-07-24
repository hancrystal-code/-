package solabo.GongGuHaSong.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {

    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name){
        Hello hello = new Hello();//new 객체 생성
        hello.setName(name);
        return hello;//setName 매소드 사용해 인자받아 설정한 객체를 반환
    }
    static class Hello{
        private String name;
        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }


    }
}
