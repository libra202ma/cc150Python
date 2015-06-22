"""
Since XML is very verbose, you are given a way of encoding it
where each tag gets mapped to a pre-defined integer value. The
language/grammar is as follows:

Element    --> Tag Attributes END Children END
Attribute  --> Tab Value
END        --> 0
Tag        --> Some predefined mapping to int
Value      --> String value END

For example, the following XML might be converted into the compressed string below (assuming a mapping of family -> 1, person -> 2, firstname -> 3, lastname -> 4, state -> 5).

<family lastName="McDowell" state="CA">
  <person firstName="Gayle">Some Message</person>
</family>

Becomes:

1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0

Write code to print the encoded version of XML element (passed in
Element and Attribute objects).
"""

encodeMap = {
    "family": 1,
    "person": 2,
    "firstName": 3,
    "lastName": 4,
    "state": 5,
}


def encodeXML(root):
    ret = ""
    # Open tag
    ret += str(encodeMap[root.tag]) + " "
    # Encode attributes
    for at in sorted(root.attrib):
        ret += str(encodeMap[at]) + " " + root.attrib[at] + " "
    # Closing bracket
    ret += "0 "
    # Encode children
    if len(root) >= 1:
        for child in root:
            ret += encodeXML(child)
    # Or encode value if no children
    else:
        ret += root.text + " "
    # Closing tag
    ret += "0 "
    return ret


def test_encodeXML():
    import xml.etree.ElementTree as ET

    root = ET.fromstring("""
    <family lastName="McDowell" state="CA">
    <person firstName="Gayle">Some Message</person>
    </family>
    """)
    assert encodeXML(root) == "1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0 "
