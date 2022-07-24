package solabo.GongGuHaSong.web.dto;

import lombok.Data;
import solabo.GongGuHaSong.domain.Board;

@Data
public class BoardSaveDto {
    private String title;
    private String content;

    public Board toEntity(){
        Board board = new Board();
        board.setTitle(title);
        board.setContent(content);
        return board;
    }
}
