import re


class CFToken:

    def __init__(self, value, line, col):
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value!r}, line={self.line}, col={self.col})'


class CFTagToken(CFToken):

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.name = value[1:-1]


class CFStringToken(CFToken):

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

    TAG_REGEX = re.compile(r'<\/?\w.*?>')
    STRING_REGEX = re.compile(r'(".*?")|(\'.*?\')')

    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        lines = self.code.split('\n')

        for line_num, line in enumerate(lines, start=1):
            self.tokenize_line(line, line_num)

        return self.tokens

    def tokenize_line(self, text, line_num):
        self.tokenize_tags(text, line_num)
        self.tokenize_strings(text, line_num)
        self.tokenize_keywords(text, line_num)
        self.tokenize_operators(text, line_num)
        self.tokenize_functions(text, line_num)
        self.tokenize_script(text, line_num)

    def tokenize_tags(self, text, line):
        for match in self.TAG_REGEX.finditer(text):
            token = CFTagToken(match.group(), line, match.start()+1)
            self.tokens.append(token)

    def tokenize_strings(self, text, line):
        for match in self.STRING_REGEX.finditer(text):
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
