```mermaid

graph TD
    subgraph Chapter
        direction TB
        2[Create section .s Title] --> Section
        subgraph Section
            direction TB
            3[Create paragraph .p Title] --> Paragraph
            subgraph Paragraph
                direction LR
                paragraph1
                paragraph2
                paragraph3
            end
        end
    end

    1[Create chapter .c Chapter title] --> Chapter
```