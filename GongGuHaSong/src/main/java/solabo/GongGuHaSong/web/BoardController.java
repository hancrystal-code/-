package solabo.GongGuHaSong.web;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import solabo.GongGuHaSong.domain.Board;
import solabo.GongGuHaSong.repository.BoardRepository;
import solabo.GongGuHaSong.web.dto.BoardSaveDto;

import java.util.List;

@RequiredArgsConstructor //DI
@RestController //데이터 리턴 서버
public class BoardController {
    //DI
    private final BoardRepository boardRepository;

    @PutMapping("board/{id}")
    public void update(@RequestBody BoardSaveDto dto, @PathVariable String id){
        Board board = dto.toEntity();
        board.set_id(id); // save함수는 같은 아이디일 시 수정
        boardRepository.save(board);
    }

    @DeleteMapping("board/{id}")
    public int deleteById(@PathVariable String id){
        boardRepository.deleteById(id);
        return 1; //1:성공, -1:실패
    }

    @GetMapping("/board/{id}")
    public Board findById(@PathVariable String id) {
        return boardRepository.findById(id).get();
    }


    @GetMapping("/board")
    public List<Board> findAll(){
        return boardRepository.findAll();
    }

    @PostMapping("/board")
    public Board save(@RequestBody BoardSaveDto dto) {
        //{"title":"제목","content":"내용"}
        //@RequsetBody 어노테이션을 붙인 이유는 json 타입으로 데이터를 받기 위함.
        Board boardEntity = boardRepository.save(dto.toEntity());
        return boardEntity;
    }
}
