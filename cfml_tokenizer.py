"""
CFMLTokenizer - Tokenizer for ColdFusion Markup Language code 

Tokens CFML code by extracting tags, strings, keywords, 
functions, script blocks etc into a token object model.

Provides nested tag support by tracking open tags during
tokenization.

"""

import re
from collections import deque


class CFToken:
    """Base token class with value, line and column"""

    def __init__(self, value, line, col):
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value!r}, line={self.line}, col={self.col})'


class CFTagToken(CFToken):
    """Represents start, end tags"""

    TAG_REGEX = re.compile(r'<(/?\w+)(.*?)>')

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.name = value[1:-1]  # Extract tag name


class CFStringToken(CFToken):

    STRING_REGEX = re.compile(r'(".*?")|(\'.*?\')')
    LITERAL = 'literal'
    SINGLE_QUOTE = 'single quote'

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.type = self.LITERAL if value.startswith(
            '"') else self.SINGLE_QUOTE


class CFOperatorToken(CFToken):

    OPERATORS = {'=': 'ASSIGN', '==': 'EQ', '!=': 'NEQ',
                 '<': 'LT', '>': 'GT', '<=': 'LTE', '>=': 'GTE',
                 '&&': 'AND', '||': 'OR', '+': 'ADD', '-': 'SUB',
                 '*': 'MUL', '/': 'DIV'}

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.type = self.OPERATORS.get(value, 'UNKNOWN')


class CFKeywordToken(CFToken):

    KEYWORDS = ['if', 'else', 'while', 'for', 'function',
                'component', 'property', 'return', 'include',
                'import', 'param', 'try', 'catch', 'interface',
                'implements']

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.keyword = value if value in self.KEYWORDS else None

    def __str__(self):
        return f'CFKeywordToken({self.keyword})' if self.keyword else 'CFKeywordToken(UNKNOWN)'


class CFFunctionToken(CFToken):

    FUNCTIONS = [
        'Abs', 'ACos', 'AddSOAPRequestHeader', 'AddSOAPResponseHeader', 'ArrayAppend',
        'ArrayAvg', 'ArrayClear', 'ArrayDeleteAt', 'ArrayInsertAt', 'ArrayIsDefined',
        'ArrayIsEmpty', 'ArrayLen', 'ArrayMax', 'ArrayMin', 'ArrayNew', 'ArrayPrepend',
        'ArrayResize', 'ArraySet', 'ArraySort', 'ArraySum', 'ArraySwap', 'ArrayToList',
        'Asc', 'ASin', 'ATan', 'Beat', 'BinaryDecode', 'BinaryEncode', 'BitAnd',
        'BitMaskClear', 'BitMaskRead', 'BitMaskSet', 'BitNot', 'BitOr', 'BitSHLN',
        'BitSHRN', 'BitXOr', 'Ceiling', 'CFusion_decrypt', 'CFusion_encrypt',
        'CharsetDecode', 'CharsetEncode', 'Chr', 'CJustify', 'Compare', 'CompareNoCase',
        'CompileRest', 'ComponentInfo', 'CompoundHash', 'ContractPath', 'Cos', 'CreateDecoder',
        'CreateObject', 'CreateUUId', 'CreateObject', 'CreateODBCDate', 'CreateODBCDateTime',
        'CreateODBCTime', 'CreateTime', 'CreateTimeSpan', 'CreateUniqueString', 'DateAdd',
        'DateCompare', 'DateConvert', 'DateDiff', 'DateFormat', 'DatePart', 'DateTimeFormat',
        'Day', 'DayOfWeek', 'DayOfWeekAsString', 'DayOfYear', 'DaysInMonth', 'DaysInYear',
        'DecrementValue', 'Decrypt', 'DecryptBinary', 'DeleteClientVariable', 'DESDecrypt',
        'DESEncrypt', 'DirectoryExists', 'DollarFormat', 'Duplicate', 'Each', 'Encrypt',
        'EncryptBinary', 'EntityDecode', 'EntityEncode', 'Exp', 'ExpandPath', 'Extract',
        'FileExists', 'Find', 'FindNoCase', 'FindOneOf', 'FirstDayOfMonth', 'Fix', 'FormatBaseN',
        'GetApplicationSettings', 'GetApplicationMetaData', 'GetAuthUser', 'GetBaseTagData',
        'GetBaseTagList', 'GetBaseTemplatePath', 'GetClientVariablesList',
        'GetComponentMetaData', 'GetContextRoot', 'GetCurrentTemplatePath',
        'GetDirectoryFromPath', 'GetEncoding', 'GetException', 'GetFileFromPath',
        'GetFileInfo', 'GetFunctionList', 'GetGatewayHelper', 'GetHttpTimeString',
        'GetK2ServerDocCount', 'GetK2ServerDocCountLimit', 'GetLocale',
        'GetLocaleDisplayName', 'GetMetaData', 'GetMetricData', 'GetPageContext',
        'GetProfileSections', 'GetProfileString', 'GetRequestData', 'GetScriptProtectNumLines',
        'GetSOAPRequest', 'GetSOAPRequestHeader', 'GetSOAPResponse',
        'GetSOAPResponseHeader', 'GetTempDirectory', 'GetTempFile', 'GetTickCount',
        'GetTimeZoneInfo', 'GetToken', 'GetTotalSpace', 'GetUserRoles', 'GetWriteableImageFormats',
        'Hash', 'Hash40', 'Hour', 'HTMLCodeFormat', 'HTMLEditFormat', 'IIf', 'ImageAddBorder',
        'ImageBlur', 'ImageClearRect', 'ImageCopy', 'ImageCreateCaptcha', 'ImageCrop',
        'ImageDilate', 'ImageDrawArc', 'ImageDrawBeveledRect', 'ImageDrawCubicCurve',
        'ImageDrawLine', 'ImageDrawLines', 'ImageDrawOval', 'ImageDrawPoint',
        'ImageDrawQuadraticCurve', 'ImageDrawRect', 'ImageDrawRoundRect', 'ImageDrawText',
        'ImageFlip', 'ImageGetBlob', 'ImageGetBufferedImage', 'ImageGetEXIFTag', 'ImageGetHeight',
        'ImageGetIPTCTag', 'ImageGetWidth', 'ImageGrayScale', 'ImageInfo', 'ImageNegative',
        'ImageNew', 'ImageOverlay', 'ImagePaste', 'ImageRead', 'ImageReadBase64',
        'ImageResize', 'ImageRotate', 'ImageRotateDrawingAxis', 'ImageScaleToFit',
        'ImageSetBackgroundColor', 'ImageSetDrawingColor', 'ImageSetDrawingStroke',
        'ImageSetDrawingTransparency', 'ImageSharpen', 'ImageShear', 'ImageShearDrawingAxis',
        'ImageTranslate', 'ImageTranslateDrawingAxis', 'ImageWrite', 'ImageWriteBase64',
        'IncrementValue', 'InputBaseN', 'Insert', 'Int', 'InvalidateOAuthaccesstoken', 'IsArray',
        'IsBinary', 'IsBoolean', 'IsCustomFunction', 'IsDate', 'IsDDX', 'IsDebugMode',
        'IsImage', 'IsImageFile', 'IsInstanceOf', 'IsJSON', 'IsLeapYear', 'IsNumeric',
        'IsNumericDate', 'IsObject', 'IsPDFFile', 'IsPDFObject', 'IsQuery',
        'IsSimpleValue', 'IsSOAPRequest', 'IsStruct', 'IsUserInAnyRole', 'IsUserInRole',
        'IsUserLoggedIn', 'IsValid', 'IsValidOauthaccesstoken', 'IsWDDX', 'IsXML', 'IsXMLAttribute',
        'IsXMLElement', 'IsXMLNode', 'IsXMLRoot', 'IsXSSFFile', 'IsXSSFPicture', 'IsXSSFShape',
        'IsXSSFSheet', 'IsXSSFWorkbook', 'JSStringFormat', 'LCase', 'Left', 'Len', 'ListAppend',
        'ListChangeDelims', 'ListContains', 'ListContainsNoCase', 'ListDeleteAt', 'ListFilter',
        'ListFind', 'ListFindNoCase', 'ListFirst', 'ListGetAt', 'ListInsertAt', 'ListLast',
        'ListLen', 'ListPrepend', 'ListQualify', 'ListReduce', 'ListRemoveDuplicates',
        'ListRest', 'ListSetAt', 'ListSort', 'ListToArray', 'ListValueCount', 'ListValueCountNoCase',
        'LJustify', 'LSParseCurrency', 'LSParseDateTime', 'LSParseEuroCurrency', 'LSParseNumber',
        'Max', 'Metaphone', 'Mid', 'Min', 'Minute', 'Month', 'MonthAsString', 'Now', 'NumberFormat',
        'ObjectEquals', 'ObjectLoad', 'ObjectSave', 'OnApplicationEnd', 'OnApplicationStart',
        'OnError', 'OnMissingMethod', 'OnMissingTemplate', 'OnRequest', 'OnRequestEnd',
        'OnRequestStart', 'OnSessionEnd', 'OnSessionStart', 'ParagraphFormat', 'ParseDateTime',
        'ParseNumber', 'Pi', 'PreserveSingleQuotes', 'Quarter', 'QueryAddColumn', 'QueryAddRow',
        'QueryColumnArray', 'QueryColumnCount', 'QueryColumnExists', 'QueryColumnList',
        'QueryConvertForGrid', 'QueryCurrentRow', 'QueryDeleteColumn', 'QueryDeleteRow',
        'QueryGetCell', 'QueryGetRow', 'QueryMap', 'QueryNew', 'QueryRecordCount', 'QueryReduce',
        'QueryRowData', 'QuerySetCell', 'Rand', 'Randomize', 'RandRange', 'REFind', 'REFindNoCase',
        'ReleaseComObject', 'RemoveChars', 'RemoveNumeric', 'RepeatString', 'Replace', 'ReplaceList',
        'ReplaceNoCase', 'REReplace', 'REReplaceNoCase', 'RESplit', 'RESplitNoCase', 'Reverse', 'RTrim',
        'Second', 'SendGatewayMessage', 'Serialize', 'SerializeJSON', 'SerializeXML', 'SessionId',
        'SessionInvalidate', 'SessionRotate', 'SessionTimeout', 'SetEncoding', 'SetLocale',
        'SetProfileString', 'SetVariable', 'Sgn', 'Sin', 'SpanExcluding', 'SpanIncluding', 'SpreadsheetAddAutoFilter',
        'SpreadsheetAddColumn', 'SpreadsheetAddFreezePane', 'SpreadsheetAddImage',
        'SpreadsheetAddInfo', 'SpreadsheetAddRow', 'SpreadsheetAddRows', 'SpreadsheetAddSplitPane',
        'SpreadsheetCreateSheet', 'SpreadsheetDeleteColumn', 'SpreadsheetDeleteColumns',
        'SpreadsheetDeleteRow', 'SpreadsheetDeleteRows', 'SpreadsheetFormatCell',
        'SpreadsheetFormatCellRange', 'SpreadsheetFormatColumn', 'SpreadsheetFormatColumns',
        'SpreadsheetFormatRow', 'SpreadsheetFormatRows', 'SpreadsheetGetCellComment',
        'SpreadsheetGetCellFormula', 'SpreadsheetGetCellValue', 'SpreadsheetInfo',
        'SpreadsheetMergeCells', 'SpreadsheetNew', 'SpreadsheetRead', 'SpreadsheetReadBinary',
        'SpreadsheetRemoveSheet', 'SpreadsheetSetActiveSheet', 'SpreadsheetSetActiveSheetNumber',
        'SpreadsheetSetCellComment', 'SpreadsheetSetCellFormula', 'SpreadsheetSetCellValue',
        'SpreadsheetSetColumnWidth', 'SpreadsheetSetFooter', 'SpreadsheetSetHeader',
        'SpreadsheetSetRowHeight', 'SpreadsheetShiftColumns', 'SpreadsheetShiftRows',
        'SpreadsheetWrite', 'Sqrt', 'StripCR', 'StructAppend', 'StructClear', 'StructCopy',
        'StructCount', 'StructDelete', 'StructEach', 'StructFilter', 'StructFind',
        'StructFindKey', 'StructFindValue', 'StructGet', 'StructInsert', 'StructIsEmpty',
        'StructKeyArray', 'StructKeyExists', 'StructKeyList', 'StructNew', 'StructSort',
        'StructUpdate', 'Tan', 'Throw', 'TimeFormat', 'ToBase64', 'ToBinary', 'ToScript', 'ToString',
        'Trace', 'TransactionCommit', 'TransactionRollback', 'Trim', 'UCase', 'URLDecode', 'URLEncodedFormat',
        'URLSessionFormat', 'Val', 'ValueArray', 'ValueList', 'VerifyClient', 'Week', 'Wrap', 'WriteBody',
        'WriteDump', 'WriteLog', 'WriteOutput', 'WSGetAllChannels', 'WSGetSubscribers', 'WSPublish',
        'WSSendMessage', 'WSSubscribe', 'WSSendMessage', 'XMLChildPos', 'XMLElemNew', 'XMLFormat',
        'XMLGetNodeType', 'XMLNew', 'XMLParse', 'XMLSearch', 'XMLTransform', 'XMLValidate',
        'Year', 'YesNoFormat'
    ]

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.function = value if value in self.FUNCTIONS else None

    def __str__(self):
        return f'CFFunctionToken({self.function})' if self.function else 'CFFunctionToken(UNKNOWN)'


class CFScriptToken(CFToken):

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.script = self._get_script(value)

    def _get_script(self, value):
        if value.startswith('<cfscript>') and value.endswith('</cfscript>'):
            return value[10:-11].strip()
        else:
            return None

    def __str__(self):
        script = self.script[:20] if self.script else 'INVALID'
        return f'CFScriptToken({script}...)'


class CFMLTokenizer:

    HTML_TAG_REGEX = re.compile(r'<(\w+)(.*?)/?>')
    CF_TAG_REGEX = re.compile(r'<cf(\w+)(.*?)/?>')

    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.open_tags = deque()  # Track open tags

    def tokenize(self):
        """Tokenize entire code by line"""
        lines = self.code.split('\n')

        for line_num, line in enumerate(lines, start=1):
            self.tokenize_line(line, line_num)

        # Validate all tags closed
        if self.open_tags:
            self.handle_unclosed_tags(line_num)

        return self.tokens

    def tokenize_line(self, text, line_num):
        """Tokenize a single line of code"""

        # Tokenize parts of CFML syntax
        self.tokenize_tags(text, line_num)
        self.tokenize_strings(text, line_num)
        self.tokenize_keywords(text, line_num)
        self.tokenize_functions(text, line_num)
        self.tokenize_script(text, line_num)

    def tokenize_tags(self, text, line_num):
        """Extract tags into tokens"""

        pos = 0
        while pos < len(text):
            
            # Check for HTML tag
            html_match = self.HTML_TAG_REGEX.match(text, pos)
            if html_match:
                # Handle HTML tag
                self.handle_html_tag(html_match, line_num)
                pos = html_match.end()
                continue
            
            # Check for CF tag 
            cf_match = self.CF_TAG_REGEX.match(text, pos)
            if cf_match:
                # Handle CF tag
                self.handle_cf_tag(cf_match, line_num)
                pos = cf_match.end()
                continue
                
            # No more tags
            break

        # Validate all CF tags closed  
        if self.open_cf_tags:
            self.handle_unclosed_cf_tags(line_num)

    # Tag handling methods
    def handle_cf_tag(self, match, line_num):
        
        tag_name = match.group(1)
        is_self_closing = match.group(2).endswith('/')
        
        if is_self_closing:
            # Handle self closing CF tag
            self.handle_self_closing_tag()
        else:
            # Handle open and close CF tags
            if tag_name.startswith('/'):
                # Closing tag
                self.handle_opening_tag()
            else:
                # Opening tag
                self.handle_closing_tag()
                
    def handle_closing_tag(self, tag, line_num):
        """Handle closing tag"""

        opening_tag = self.open_tags.pop()
        if opening_tag != tag[1:]:
            print(f"Error: {tag} does not match {opening_tag} at {line_num}")

        closing_tag_token = CFTagToken(tag, line_num, 0)
        self.tokens.append(closing_tag_token)

    def handle_opening_tag(self, tag, attrs, line_num):
        """Handle opening tag"""

        opening_tag_token = CFTagToken(f"<{tag}{attrs}>", line_num, 0)
        self.tokens.append(opening_tag_token)
        self.open_tags.append(tag)

    def handle_unclosed_tags(self, line_num):
        """Handle tags not closed at end"""
        print(f"Error: Unclosed tags at end: {self.open_tags}")

    def tokenize_strings(self, text, line):
        for match in CFStringToken.STRING_REGEX.finditer(text):
            token = CFStringToken(match.group(), line, match.start()+1)
            self.tokens.append(token)

    def tokenize_keywords(self, text, line):
        for word in CFKeywordToken.KEYWORDS:
            for match in re.finditer(rf'\\b{word}\\b', text):
                token = CFKeywordToken(word, line, match.start()+1)
                self.tokens.append(token)

    def tokenize_functions(self, text, line):
        for func in CFFunctionToken.FUNCTIONS:
            if func in text:
                token = CFFunctionToken(func, line, text.find(func))
                self.tokens.append(token)

    def tokenize_script(self, text, line):
        idx = text.find('<cfscript>')
        if idx != -1:
            script = text[idx+10:-11]
            token = CFScriptToken(script, line, idx)
            self.tokens.append(token)
