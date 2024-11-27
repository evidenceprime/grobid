package org.grobid.core.document;

import nu.xom.Element;
import org.grobid.core.analyzers.GrobidAnalyzer;
import org.grobid.core.data.Note;
import org.grobid.core.layout.LayoutToken;
import org.grobid.core.utilities.GrobidProperties;
import org.grobid.core.utilities.LayoutTokensUtil;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.List;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertThat;

public class TEIFormatterTest {

    @BeforeClass
    public static void setInitialContext() throws Exception {
        GrobidProperties.getInstance();
    }

    @Test
    public void testMakeFootNote() throws Exception {

        String text = "1 This is a footnote";
        List<LayoutToken> tokens = GrobidAnalyzer.getInstance().tokenizeWithLayoutToken(text);

        List<Note> footnotes = new TEIFormatter(null, null).makeNotes(tokens, text, Note.NoteType.FOOT, 0);
        assertThat(footnotes.size(), is(1));

        Note footnote = footnotes.get(0);

        assertThat(footnote.getText(), is("This is a footnote"));
        assertThat(LayoutTokensUtil.toText(footnote.getTokens()), is("This is a footnote"));
        assertThat(footnote.getLabel(), is("1"));
    }


    @Test
    public void testMakeNotes() throws Exception {
        String text = "198 U.S. Const. art. I,  § §9 & 10. \n199 To be sure, there are revisionist arguments that the Ex Post Facto clause itself extends to retroactive civil laws too. See Eastern Enterprises v. Apfel, 524 U.S. 498, 538-39 (1998) (Thomas, J., concurring). And as with bills of attainder, in the wake of the Civil War the Supreme Court held that Ironclad  Oath requirements were ex post facto laws as well. Cummings, 71 U.S. at 326-332; Garland, 71 U.S.  at 377-368. But as discussed in the text, even these principles do not ensnare Section Three going  forward, on a non-ex-post-facto basis \n200 3 U.S. at 378-80 (arguments of counsel). \n201 Id. \n202 Id. at 382. See Baude & Sachs, Eleventh Amendment, supra note 9, at 626-627.   Electronic copy available at: https://ssrn.com/abstract=4532751";
        List<LayoutToken> tokens = GrobidAnalyzer.getInstance().tokenizeWithLayoutToken(text);
        text = text.replace("\n", " ");
        tokens.stream().forEach(t -> t.setOffset(t.getOffset() + 403));
        List<Note> footnotes = new TEIFormatter(null, null)
            .makeNotes(tokens, text, Note.NoteType.FOOT, 37);

        assertThat(footnotes, hasSize(5));
        assertThat(footnotes.get(0).getLabel(), is("198"));
        assertThat(footnotes.get(0).getTokens(), hasSize(greaterThan(0)));
        assertThat(footnotes.get(1).getLabel(), is("199"));
        assertThat(footnotes.get(1).getTokens(), hasSize(greaterThan(0)));
        assertThat(footnotes.get(2).getLabel(), is("200"));
        assertThat(footnotes.get(2).getTokens(), hasSize(greaterThan(0)));
        assertThat(footnotes.get(3).getLabel(), is("201"));
        assertThat(footnotes.get(3).getText(), is("Id. "));
        assertThat(footnotes.get(3).getTokens(), hasSize(greaterThan(0)));
        assertThat(footnotes.get(4).getLabel(), is("202"));
        assertThat(footnotes.get(4).getTokens(), hasSize(greaterThan(0)));
    }

    @Test
    public void testGenerateURLRef() throws Exception {
        String input = "http:// github.com/ lfoppiano/ grobid-bla";
        List<LayoutToken> tokens = GrobidAnalyzer.getInstance().tokenizeWithLayoutToken(input);

        Element node = new TEIFormatter(null, null)
            .generateURLRef("http:// github.com/ lfoppiano/ grobid-bla", tokens, false);

        assertThat(node.toXML(), is("<ref xmlns=\"http://www.tei-c.org/ns/1.0\" type=\"url\" target=\"http://github.com/lfoppiano/grobid-bla\">http:// github.com/ lfoppiano/ grobid-bla</ref>"));
    }


}