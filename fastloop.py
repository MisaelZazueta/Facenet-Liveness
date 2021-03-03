def loop (f_x = {}, arr=[]):
    for i in range(256):
        f_x[i] = 0
    for j in range(len(arr)):
        x = arr[j]
        f_x[x] += 1
        '''
    for i in range(256):
        if arr[i] == 0:
            f_x[0] += 1
        elif arr[i] == 1:
            f_x[1] += 1
        elif arr[i] == 2:
            f_x[2] += 1
        elif arr[i] == 3:
            f_x[3] += 1
        elif arr[i] == 4:
            f_x[4] += 1
        elif arr[i] == 5:
            f_x[5] += 1
        elif arr[i] == 6:
            f_x[6] += 1
        elif arr[i] == 7:
            f_x[7] += 1
        elif arr[i] == 8:
            f_x[8] += 1
        elif arr[i] == 9:
            f_x[9] += 1
        elif arr[i] == 10:
            f_x[10] += 1
        elif arr[i] == 11:
            f_x[11] += 1
        elif arr[i] == 12:
            f_x[12] += 1
        elif arr[i] == 13:
            f_x[13] += 1
        elif arr[i] == 14:
            f_x[14] += 1
        elif arr[i] == 15:
            f_x[15] += 1
        elif arr[i] == 16:
            f_x[16] += 1
        elif arr[i] == 17:
            f_x[17] += 1
        elif arr[i] == 18:
            f_x[18] += 1
        elif arr[i] == 19:
            f_x[19] += 1
        elif arr[i] == 20:
            f_x[20] += 1
        elif arr[i] == 21:
            f_x[21] += 1
        elif arr[i] == 22:
            f_x[22] += 1
        elif arr[i] == 23:
            f_x[23] += 1
        elif arr[i] == 24:
            f_x[24] += 1
        elif arr[i] == 25:
            f_x[25] += 1
        elif arr[i] == 26:
            f_x[26] += 1
        elif arr[i] == 27:
            f_x[27] += 1
        elif arr[i] == 28:
            f_x[28] += 1
        elif arr[i] == 29:
            f_x[29] += 1
        elif arr[i] == 30:
            f_x[30] += 1
        elif arr[i] == 31:
            f_x[31] += 1
        elif arr[i] == 32:
            f_x[32] += 1
        elif arr[i] == 33:
            f_x[33] += 1
        elif arr[i] == 34:
            f_x[34] += 1
        elif arr[i] == 35:
            f_x[35] += 1
        elif arr[i] == 36:
            f_x[36] += 1
        elif arr[i] == 37:
            f_x[37] += 1
        elif arr[i] == 38:
            f_x[38] += 1
        elif arr[i] == 39:
            f_x[39] += 1
        elif arr[i] == 40:
            f_x[40] += 1
        elif arr[i] == 41:
            f_x[41] += 1
        elif arr[i] == 42:
            f_x[42] += 1
        elif arr[i] == 43:
            f_x[43] += 1
        elif arr[i] == 44:
            f_x[44] += 1
        elif arr[i] == 45:
            f_x[45] += 1
        elif arr[i] == 46:
            f_x[46] += 1
        elif arr[i] == 47:
            f_x[47] += 1
        elif arr[i] == 48:
            f_x[48] += 1
        elif arr[i] == 49:
            f_x[49] += 1
        elif arr[i] == 50:
            f_x[50] += 1
        elif arr[i] == 51:
            f_x[51] += 1
        elif arr[i] == 52:
            f_x[52] += 1
        elif arr[i] == 53:
            f_x[53] += 1
        elif arr[i] == 54:
            f_x[54] += 1
        elif arr[i] == 55:
            f_x[55] += 1
        elif arr[i] == 56:
            f_x[56] += 1
        elif arr[i] == 57:
            f_x[57] += 1
        elif arr[i] == 58:
            f_x[58] += 1
        elif arr[i] == 59:
            f_x[59] += 1
        elif arr[i] == 60:
            f_x[60] += 1
        elif arr[i] == 61:
            f_x[61] += 1
        elif arr[i] == 62:
            f_x[62] += 1
        elif arr[i] == 63:
            f_x[63] += 1
        elif arr[i] == 64:
            f_x[64] += 1
        elif arr[i] == 65:
            f_x[65] += 1
        elif arr[i] == 66:
            f_x[66] += 1
        elif arr[i] == 67:
            f_x[67] += 1
        elif arr[i] == 68:
            f_x[68] += 1
        elif arr[i] == 69:
            f_x[69] += 1
        elif arr[i] == 70:
            f_x[70] += 1
        elif arr[i] == 71:
            f_x[71] += 1
        elif arr[i] == 72:
            f_x[72] += 1
        elif arr[i] == 73:
            f_x[73] += 1
        elif arr[i] == 74:
            f_x[74] += 1
        elif arr[i] == 75:
            f_x[75] += 1
        elif arr[i] == 76:
            f_x[76] += 1
        elif arr[i] == 77:
            f_x[77] += 1
        elif arr[i] == 78:
            f_x[78] += 1
        elif arr[i] == 79:
            f_x[79] += 1
        elif arr[i] == 80:
            f_x[80] += 1
        elif arr[i] == 81:
            f_x[81] += 1
        elif arr[i] == 82:
            f_x[82] += 1
        elif arr[i] == 83:
            f_x[83] += 1
        elif arr[i] == 84:
            f_x[84] += 1
        elif arr[i] == 85:
            f_x[85] += 1
        elif arr[i] == 86:
            f_x[86] += 1
        elif arr[i] == 87:
            f_x[47] += 1
        elif arr[i] == 88:
            f_x[88] += 1
        elif arr[i] == 89:
            f_x[89] += 1
        elif arr[i] == 90:
            f_x[90] += 1
        elif arr[i] == 91:
            f_x[91] += 1
        elif arr[i] == 92:
            f_x[92] += 1
        elif arr[i] == 93:
            f_x[93] += 1
        elif arr[i] == 94:
            f_x[94] += 1
        elif arr[i] == 95:
            f_x[95] += 1
        elif arr[i] == 96:
            f_x[96] += 1
        elif arr[i] == 97:
            f_x[97] += 1
        elif arr[i] == 98:
            f_x[98] += 1
        elif arr[i] == 99:
            f_x[99] += 1
        elif arr[i] == 100:
            f_x[100] += 1
        elif arr[i] == 101:
            f_x[101] += 1
        elif arr[i] == 102:
            f_x[102] += 1
        elif arr[i] == 103:
            f_x[103] += 1
        elif arr[i] == 104:
            f_x[104] += 1
        elif arr[i] == 105:
            f_x[105] += 1
        elif arr[i] == 106:
            f_x[106] += 1
        elif arr[i] == 107:
            f_x[107] += 1
        elif arr[i] == 108:
            f_x[108] += 1
        elif arr[i] == 109:
            f_x[109] += 1
        elif arr[i] == 110:
            f_x[110] += 1
        elif arr[i] == 111:
            f_x[111] += 1
        elif arr[i] == 112:
            f_x[112] += 1
        elif arr[i] == 113:
            f_x[113] += 1
        elif arr[i] == 114:
            f_x[114] += 1
        elif arr[i] == 115:
            f_x[115] += 1
        elif arr[i] == 116:
            f_x[116] += 1
        elif arr[i] == 117:
            f_x[117] += 1
        elif arr[i] == 118:
            f_x[118] += 1
        elif arr[i] == 119:
            f_x[119] += 1
        elif arr[i] == 120:
            f_x[120] += 1
        elif arr[i] == 121:
            f_x[121] += 1
        elif arr[i] == 122:
            f_x[122] += 1
        elif arr[i] == 123:
            f_x[123] += 1
        elif arr[i] == 124:
            f_x[124] += 1
        elif arr[i] == 125:
            f_x[125] += 1
        elif arr[i] == 126:
            f_x[126] += 1
        elif arr[i] == 127:
            f_x[127] += 1
        elif arr[i] == 128:
            f_x[128] += 1
        elif arr[i] == 129:
            f_x[129] += 1
        elif arr[i] == 130:
            f_x[130] += 1
        elif arr[i] == 131:
            f_x[131] += 1
        elif arr[i] == 132:
            f_x[132] += 1
        elif arr[i] == 133:
            f_x[133] += 1
        elif arr[i] == 134:
            f_x[134] += 1
        elif arr[i] == 135:
            f_x[135] += 1
        elif arr[i] == 136:
            f_x[136] += 1
        elif arr[i] == 137:
            f_x[137] += 1
        elif arr[i] == 138:
            f_x[138] += 1
        elif arr[i] == 139:
            f_x[139] += 1
        elif arr[i] == 140:
            f_x[140] += 1
        elif arr[i] == 141:
            f_x[141] += 1
        elif arr[i] == 142:
            f_x[142] += 1
        elif arr[i] == 143:
            f_x[143] += 1
        elif arr[i] == 144:
            f_x[144] += 1
        elif arr[i] == 145:
            f_x[145] += 1
        elif arr[i] == 146:
            f_x[146] += 1
        elif arr[i] == 147:
            f_x[147] += 1
        elif arr[i] == 148:
            f_x[148] += 1
        elif arr[i] == 149:
            f_x[149] += 1
        elif arr[i] == 150:
            f_x[150] += 1
        elif arr[i] == 151:
            f_x[151] += 1
        elif arr[i] == 152:
            f_x[152] += 1
        elif arr[i] == 153:
            f_x[153] += 1
        elif arr[i] == 154:
            f_x[154] += 1
        elif arr[i] == 155:
            f_x[155] += 1
        elif arr[i] == 156:
            f_x[156] += 1
        elif arr[i] == 157:
            f_x[157] += 1
        elif arr[i] == 158:
            f_x[158] += 1
        elif arr[i] == 159:
            f_x[159] += 1
        elif arr[i] == 160:
            f_x[160] += 1
        elif arr[i] == 161:
            f_x[161] += 1
        elif arr[i] == 162:
            f_x[162] += 1
        elif arr[i] == 163:
            f_x[163] += 1
        elif arr[i] == 164:
            f_x[164] += 1
        elif arr[i] == 165:
            f_x[165] += 1
        elif arr[i] == 166:
            f_x[166] += 1
        elif arr[i] == 167:
            f_x[167] += 1
        elif arr[i] == 168:
            f_x[168] += 1
        elif arr[i] == 169:
            f_x[169] += 1
        elif arr[i] == 170:
            f_x[170] += 1
        elif arr[i] == 171:
            f_x[171] += 1
        elif arr[i] == 172:
            f_x[172] += 1
        elif arr[i] == 173:
            f_x[173] += 1
        elif arr[i] == 174:
            f_x[174] += 1
        elif arr[i] == 175:
            f_x[175] += 1
        elif arr[i] == 176:
            f_x[176] += 1
        elif arr[i] == 177:
            f_x[177] += 1
        elif arr[i] == 178:
            f_x[178] += 1
        elif arr[i] == 179:
            f_x[179] += 1
        elif arr[i] == 180:
            f_x[180] += 1
        elif arr[i] == 181:
            f_x[181] += 1
        elif arr[i] == 182:
            f_x[182] += 1
        elif arr[i] == 183:
            f_x[183] += 1
        elif arr[i] == 184:
            f_x[184] += 1
        elif arr[i] == 185:
            f_x[185] += 1
        elif arr[i] == 186:
            f_x[186] += 1
        elif arr[i] == 187:
            f_x[187] += 1
        elif arr[i] == 188:
            f_x[188] += 1
        elif arr[i] == 189:
            f_x[189] += 1
        elif arr[i] == 190:
            f_x[190] += 1
        elif arr[i] == 191:
            f_x[191] += 1
        elif arr[i] == 192:
            f_x[192] += 1
        elif arr[i] == 193:
            f_x[193] += 1
        elif arr[i] == 194:
            f_x[194] += 1
        elif arr[i] == 195:
            f_x[195] += 1
        elif arr[i] == 196:
            f_x[196] += 1
        elif arr[i] == 197:
            f_x[197] += 1
        elif arr[i] == 198:
            f_x[198] += 1
        elif arr[i] == 199:
            f_x[199] += 1
        elif arr[i] == 200:
            f_x[200] += 1
        elif arr[i] == 201:
            f_x[201] += 1
        elif arr[i] == 202:
            f_x[202] += 1
        elif arr[i] == 203:
            f_x[203] += 1
        elif arr[i] == 204:
            f_x[204] += 1
        elif arr[i] == 205:
            f_x[205] += 1
        elif arr[i] == 206:
            f_x[206] += 1
        elif arr[i] == 207:
            f_x[207] += 1
        elif arr[i] == 208:
            f_x[208] += 1
        elif arr[i] == 209:
            f_x[209] += 1
        elif arr[i] == 210:
            f_x[210] += 1
        elif arr[i] == 211:
            f_x[211] += 1
        elif arr[i] == 212:
            f_x[212] += 1
        elif arr[i] == 213:
            f_x[213] += 1
        elif arr[i] == 214:
            f_x[214] += 1
        elif arr[i] == 215:
            f_x[215] += 1
        elif arr[i] == 216:
            f_x[216] += 1
        elif arr[i] == 217:
            f_x[217] += 1
        elif arr[i] == 218:
            f_x[218] += 1
        elif arr[i] == 219:
            f_x[219] += 1
        elif arr[i] == 220:
            f_x[220] += 1
        elif arr[i] == 221:
            f_x[221] += 1
        elif arr[i] == 222:
            f_x[222] += 1
        elif arr[i] == 223:
            f_x[223] += 1
        elif arr[i] == 224:
            f_x[224] += 1
        elif arr[i] == 225:
            f_x[225] += 1
        elif arr[i] == 226:
            f_x[226] += 1
        elif arr[i] == 227:
            f_x[227] += 1
        elif arr[i] == 228:
            f_x[228] += 1
        elif arr[i] == 229:
            f_x[229] += 1
        elif arr[i] == 230:
            f_x[230] += 1
        elif arr[i] == 231:
            f_x[231] += 1
        elif arr[i] == 232:
            f_x[232] += 1
        elif arr[i] == 233:
            f_x[233] += 1
        elif arr[i] == 234:
            f_x[234] += 1
        elif arr[i] == 235:
            f_x[235] += 1
        elif arr[i] == 236:
            f_x[236] += 1
        elif arr[i] == 237:
            f_x[237] += 1
        elif arr[i] == 238:
            f_x[238] += 1
        elif arr[i] == 239:
            f_x[239] += 1
        elif arr[i] == 240:
            f_x[240] += 1
        elif arr[i] == 241:
            f_x[241] += 1
        elif arr[i] == 242:
            f_x[242] += 1
        elif arr[i] == 243:
            f_x[243] += 1
        elif arr[i] == 244:
            f_x[244] += 1
        elif arr[i] == 245:
            f_x[245] += 1
        elif arr[i] == 246:
            f_x[246] += 1
        elif arr[i] == 247:
            f_x[247] += 1
        elif arr[i] == 248:
            f_x[248] += 1
        elif arr[i] == 249:
            f_x[249] += 1
        elif arr[i] == 250:
            f_x[250] += 1
        elif arr[i] == 251:
            f_x[251] += 1
        elif arr[i] == 252:
            f_x[252] += 1
        elif arr[i] == 253:
            f_x[253] += 1
        elif arr[i] == 254:
            f_x[254] += 1
        elif arr[i] == 255:
            f_x[255] += 1
            '''
    return f_x